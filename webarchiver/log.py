import logging

from webarchiver.config import *


class Log:
    """The logger."""

    def __init__(self, file_handler=True, stream_handler=True):
        """Inits the logger.

        Creates the formatter for the logger and adds file and/or stream
        handlers.

        Args:
            file_handler (bool, optional): Whether to add a file handler to the
                logger. Default is True.
            stream_handler (bool, optional): Whether to add a stream handler to
                the logger. Default is True.
        """
        logger = logging.getLogger()
        logger.setLevel(logging.NOTSET)
        logger.filter('webarchiver')
        if file_handler:
            logger.addHandler(self._init_file_handler())
        if stream_handler:
            logger.addHandler(self._init_stream_handler())
        logger.info('Started logging.')

    def _init_file_handler(self):
        """Adds the file handler to the logger.

        This will log to the file ``LOG_FILENAME`` using the created formatter.

        Returns:
            :obj:`logging.FileHandler`: The file handler.
        """
        handler = logging.FileHandler(LOG_FILENAME)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(threadName)s -'
                                               ' %(name)s - %(levelname)s -'
                                               ' %(message)s'))
        return handler

    def _init_stream_handler(self):
        """Adds the stream handler to the logger.

        This will log to stdout using the created formatter.

        Returns:
            :obj:`logging.StreamHandler`: The stream handler.
        """
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        return handler

    def shutdown(self):
        logging.info('Logging stopping.')
        logging.shutdown()
