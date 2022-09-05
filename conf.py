from os import path

YEAR = '2022'
MONTH = '08'  # 01, 02 ... 11, 12

WORK_PATH = (path.dirname(path.realpath(__file__)))
EXE_FILE_NAME = f'{YEAR}-{MONTH}.exe'

# network
STORAGE_URL = 'https://agent.beeline.ru/abh/?section=storage'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
SSL_VERIFY = False
