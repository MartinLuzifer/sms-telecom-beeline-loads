import json
import os
from subprocess import Popen

from conf import *

try:
    os.mkdir(f'{WORK_PATH}/output1')
except FileExistsError:
    pass

try:  # Загрузка учеток
    with open(f'{WORK_PATH}/account.json', 'r') as file:
        accounts = json.loads(str(file.read()))
except FileNotFoundError:
    print('Отсутствует файл account.json \n')
    raise f'Создайте файл account.json'

if __name__ == '__main__':

    for account in accounts:

        try:
            os.mkdir(f'{WORK_PATH}/output1/{account["account"]}')
        except FileExistsError:
            pass

        archive_name = f'{WORK_PATH}/archive/{account["account"]}-{EXE_FILE_NAME}'
        pdf_dir = f'{WORK_PATH}/output1/{account["account"]}'

        Popen(args=(f'{archive_name}', '/s'), cwd=pdf_dir).wait()
