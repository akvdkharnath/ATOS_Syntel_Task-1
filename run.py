#!/usr/bin/env python
# --coding:utf-8 --
'''
@File    :   run.py
@Time    :   2022/02/04 08:41:19
@Author  :   Harnath 
@Version :   1.0
@Contact :   akvdkharnath@gmail.com
@License :   © Copyright 2021 Harnath Atmakuri. All rights reserved
@Desc    :   Script which moniter input folder and logs all file entries into combined.csv
'''

COMBINED_FILE_PATH = 'combined.csv'
INPUT_FOLDER_PATH = 'input'
COMBINED_FILE_COLUMNS = ['No', 'Environment']
import os, time
import pandas as pd


def main() -> None:
    """
    Moniters input folder and and logs all file entries into combined.csv
    """

    path_to_watch = INPUT_FOLDER_PATH
    # old_files_list = os.listdir(path_to_watch)
    while 1:
        time.sleep(2)
        new_files_list = os.listdir(path_to_watch)
        data =  [[index + 1, file] for index, file in enumerate(new_files_list)]
        print(data)
        df = pd.DataFrame(data, columns = COMBINED_FILE_COLUMNS)
        df.to_csv(COMBINED_FILE_PATH, index=False)
        

if __name__ == "__main__":
    main()

