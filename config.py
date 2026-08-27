import configparser

# Load config
config = configparser.ConfigParser()
config.read('config.ini')

STORAGE_PATH = config.get('Extractor', 'storage_path')
EXTRACT_FOLDER = config.get('Extractor', 'extract_folder')
MAX_CSS = config.getint('Extractor', 'max_css')
MAX_JS = config.getint('Extractor', 'max_js')
TIMEOUT = config.getint('Extractor', 'timeout')
USER_AGENT = config.get('Extractor', 'user_agent')

[Extractor]
# Root storage path (Android's internal storage)
storage_path = /storage/emulated/0

# Folder name where extracted websites will be saved (inside storage_path)
extract_folder = Dgtl

# Maximum CSS files to download
max_css = 30

# Maximum JavaScript files to download
max_js = 30

# Connection timeout (seconds)
timeout = 20

# User-Agent to mimic a mobile browser
user_agent = Mozilla/5.0 (Linux; Android 10; Termux) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36