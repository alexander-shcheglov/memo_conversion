# coding utf:8

import http.client
import pandas as pd
import py7zr
from io import BytesIO
from urllib import request
from environs import Env
from memo_conversion.data_processor import MemoDataProcessor

MEMO_PATH = "https://github.com/MemorialInternational/memorial_data_FULL_DB/" \
            "raw/master/data/lists.memo.ru-disk/memorial_lists.tsv.7z"
MEMO_FILE_NAME = "memorial_lists.tsv"

env = Env()
env.read_env()


class MemoLoader:
    @classmethod
    def load_data(cls):
        response: 'http.client.HTTPResponse' = request.urlopen(env('MEMO_PATH', MEMO_PATH))
        buf = response.read()
        response.close()
        df: pd.DataFrame
        with py7zr.SevenZipFile(
                BytesIO(buf),
                mode='r'
        ) as arch:
            files = arch.read(targets=[env('MEMO_FILE_NAME', MEMO_FILE_NAME)])
            if MEMO_FILE_NAME in files:
                df = pd.read_csv(
                    files[MEMO_FILE_NAME],
                    header=0,
                    sep="\t",
                    quotechar="'",
                    quoting=3,
                    low_memory=False
                )
            del files
            proc = MemoDataProcessor(dataframe=df)
            proc.process_dataframe()
            return proc

