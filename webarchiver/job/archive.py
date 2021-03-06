"""Archives data from the internet."""
import logging
import os
import shutil
import subprocess
import time

from webarchiver.config import *
from webarchiver.utils import sha512_file
from webarchiver.warc import WarcFile

logger = logging.getLogger(__name__)


class ArchiveUrls:
    """Archives URLs.

    Attributes:
        urls (list of str): List of URLs to archive.
        directory (str): Directory where the files from the crawl are stored.
    """

    def __init__(self, directory, urls):
        """Inits the archival of URLs.

        If the directory for the fiels from the crawl does not exist it will be
        created.

        Args:
            urls (list of str): List of URLs to archive.
            directory (str): Directory where the files from the crawl are
                stored.
        """
        self.urls = urls
        self.directory = directory
        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)
        logger.debug('Created URL archive job %s.', self)

    def run(self):
        """Runs the crawl.

        An archive jobs is started and the return code is checked against the
        allowed list of return codes. The resulting WARC is deduplicated and
        URLs are extracted.

        Yields:
            set of tuples: Each tuple consists of the parent URL and discovered
                URL.
            bool: If the return code from the crawl is not in the list of
                allowed return codes, False is returned.
        """
        logger.debug('Starting URL archive job %s.', self)
        wget_exit_code = self.archive()
        logger.debug('Wget for URL archive job %s exited with code %s.',
                     self, wget_exit_code)
        if wget_exit_code not in WGET_EXIT_CODES:
            logger.warning('Wget for archiver job %s exited with a bad code.',
                           self)
            return False
        self.warc_file.deduplicate = True
        self.warc_file.process()
        return set(self.warc_file.extract_urls())

    def archive(self):
        """Runs a crawl job.

        Set the environment variables for the crawl and run the crawl.

        Returns:
            int: The return code of the crawl.
        """
        logger.debug('Running URL archive job %s using arguments %s.', self,
                     self.arguments)
        return subprocess.call(self.arguments)

    @property
    def warc_file(self):
        """:obj:`webarchiver.warc.WarcFile`: The WARC file object."""
        if not hasattr(self, '_warc_file'):
            self._warc_file = WarcFile(os.path.join(self.directory, [n for n in os.listdir(self.directory) if n.endswith('warc.gz')][0]))
        return self._warc_file

    @property
    def arguments(self):
        """list: Argument for the crawl.""" #TODO extend doc with options in list
        if not hasattr(self, '_arguments'):
            arguments = [
                WGET_EXECUTABLE,
                '--user-agent', USER_AGENT,
                '--no-cookies',
                '--no-check-certificate',
                '--output-file', os.path.join(self.directory, WGET_LOG),
                '--output-document', os.path.join(self.directory, WGET_TEMP),
                '--execute', 'robots=off',
                '--timeout', WGET_TIMEOUT,
                '--tries', WGET_TRIES,
                '--waitretry', WGET_WAITRETRY,
                '--warc-file', os.path.join(self.directory,
                                            os.path.basename(self.directory)),
                '--warc-header', 'operator: Archive Team',
                '--warc-header', 'archiver-version: {}'.format(VERSION),
            ]
            for url in self.urls:
                arguments.extend([
                    '--warc-header', 'source-url: {}'.format(url),
                ])
            for filename in FILES:
                arguments.extend([
                    '--warc-header',
                    'hash-{}: {}'.format(filename, sha512_file(filename))
                ])
            for url in self.urls:
                arguments.append(url)                          
            self._arguments = arguments
        return self._arguments

    def __repr__(self):
        return '<{} at 0x{:x} directory={}>'.format(__name__, id(self),
                                                    self.directory)

