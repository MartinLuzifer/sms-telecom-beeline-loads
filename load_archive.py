import json
import os
import re
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

from conf import *

if SSL_VERIFY is False:
    urllib3.disable_warnings(InsecureRequestWarning)
    print('<<<WARNING>>> InsecureRequestWarning: Unverified HTTPS request is being made to host')


def load_archive(url: str, login: str, password: str):

    with requests.session() as session:

        session.auth = HTTPBasicAuth(username=login, password=password)
        session.verify = SSL_VERIFY
        session.stream = True
        session.headers.update(HEADERS)
        response_text = session.get(url)

        return session.get(
            f'https://agent.beeline.ru/abh/{re.search(f"storage/(.*?)/{EXE_FILE_NAME}", response_text.text).group(0)}'
        )


if __name__ == '__main__':
    
    try:  # Загрузка учеток
        with open(f'{WORK_PATH}/account.json', 'r') as file:
            accounts = json.loads(str(file.read()))
    except FileNotFoundError:
        print('Отсутствует файл account.json \n')
        raise f'Создайте файл account.json'

    for account in accounts:

        try:
            os.mkdir(f'{WORK_PATH}/archive')
        except FileExistsError:
            pass
        filename = f'{WORK_PATH}/archive/{account["account"]}-{EXE_FILE_NAME}'

        try:
            open(filename, 'r')

        except FileNotFoundError:
            binary_data = load_archive(
                url='https://agent.beeline.ru/abh/?section=storage',
                login=account['login'],
                password=account['password']
            )

            print(f"Загрузка архива: {filename}")
            with open(filename, 'wb') as handle:
                for block in binary_data.iter_content(1024):
                    handle.write(block)

        else:  # not write, because file already exists
            print(f'<<<WARNING>>> File {filename} already exists: SKIP')