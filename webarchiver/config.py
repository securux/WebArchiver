"""Configuration."""
import os
import time

# crawler
REQUEST_STAGER_TIME = 120
REQUEST_UPLOAD_TIME = 5
PING_TIME = 60
MAX_BACKUPS = 3
MAX_STAGER = 5
MAX_SPACE = 1000000000

LOGS_DIRECTORY = 'logs'
LOG_FILENAME = os.path.join(LOGS_DIRECTORY,
                            'log-{}.log'.format(str(int(time.time()))))

URL_QUOTA_TIME = 2
FOUND_URLS_FILE = 'found'

LISTEN_QUEUE = 300

NEW_JOBS_DIR = 'jobs'
JOB_MAX_URLS = 1000
JOB_MAX_WAIT = 300
JOB_MAX_WAIT_URLS = 30
JOBS_CHECK_TIME = 5

CRAWLER_MIN_URL_QUOTA = 100
CRAWL_SCRIPTS = 'crawl'
CRAWLS_NEW_URLS_FILE = 'new_urls.txt'
CRAWLS_DIRECTORY = 'data'
WGET_LUA_RETURN_CODES = [0, 4, 8]
WGET_LUA_FILENAME = os.path.join(CRAWL_SCRIPTS, 'wget-lua')
LUA_SCRIPT_FILENAME = 'wget.lua'
LUA_SCRIPT_TABLE_SHOW_FILENAME = 'table_show.lua'
LUA_SCRIPT_URLCODE_FILENAME = 'urlcode.lua'
LUA_SCRIPT_JSON_FILENAME = 'JSON.lua'
LUA_SCRIPT_PATH = os.path.join(CRAWL_SCRIPTS, LUA_SCRIPT_FILENAME)
LUA_SCRIPT_TABLE_SHOW_PATH = os.path.join(CRAWL_SCRIPTS, LUA_SCRIPT_TABLE_SHOW_FILENAME)
LUA_SCRIPT_URLCODE_PATH = os.path.join(CRAWL_SCRIPTS, LUA_SCRIPT_URLCODE_FILENAME)
LUA_SCRIPT_JSON_PATH = os.path.join(CRAWL_SCRIPTS, LUA_SCRIPT_JSON_FILENAME)
LUA_SCRIPT_CHECK_TIME = None
USER_AGENT = 'ArchiveTeam; Googlebot/2.1'
WGET_LOG = 'wget.log'
WGET_TEMP = 'wget.tmp'
WGET_TIMEOUT = '30'
WGET_WAITRETRY = '30'
VERSION = '0.0.1'
DEDUPLICATION_SERVER = None
FILES = []
#FILES = [
#    'archive.py',
#    'config.py',
#    'main.py',
#    'request.py',
#    'session.py',
#    'utils.py',
#    'warc.py',
#    'server.py',
#    LUA_SCRIPT_PATH,
#    LUA_SCRIPT_TABLE_SHOW_PATH,
#    LUA_SCRIPT_URLCODE_PATH,
#    LUA_SCRIPT_JSON_PATH
#]

DEFAULT_CRAWLER_SERVER_CONFIG = {
    'confirmed': False
}

DEFAULT_CRAWLER_SERVER_CONFIG = {
    'confirmed': False
}
