import json
import os
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfMerger
from conf import *

try:  # Загрузка учеток
    with open(f'{WORK_PATH}/account.json', 'r') as file:
        accounts = json.loads(str(file.read()))
except FileNotFoundError:
    print('Отсутствует файл account.json \n')
    raise f'Создайте файл account.json'


def merge_pdf(files: list | list, destination: str):

    merger = PdfMerger()
    for pdf in list(files):
        merger.append(pdf)
    merger.write(destination)
    merger.close()


if int(MONTH) < 10:
    MONTH = MONTH[1]

print(MONTH)

for account in accounts:
    pdf_dir = f'{WORK_PATH}/output1/{account["account"]}'
    result_dir = f'{WORK_PATH}/output2'
    try:
        os.mkdir(result_dir)
    except FileExistsError:
        pass

    all_files = [f for f in listdir(pdf_dir) if isfile(join(pdf_dir, f)) and f[-3:].lower() == 'pdf']

    while len(all_files) > 4:
        file_list = []
        prefix = all_files[0][0:all_files[0].find('_')]

        for one in list(all_files):
            if prefix in one:
                print(f"Добавление {one}")
                file_list.append(f"{pdf_dir}/{one}")
                all_files.remove(one)

        merge_pdf(
            [
                file_list[2],
                file_list[3],
                file_list[0],
                file_list[1]
            ],
            f'{result_dir}/{prefix[1: len(prefix)]}_{YEAR}_{MONTH}.pdf'
        )
        print(f'Файлы Склеены в {result_dir}{prefix}_{YEAR}_{MONTH}.pdf')

