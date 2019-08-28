import json
import pandas as pd
from conf import settings
import os

def save_json(username,user_dic):
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')
    with open(user_path, 'w', encoding='utf8') as fw:
        json.dump(user_dic, fw)
        return True


def read_json(username):
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')
    with open(user_path, 'r', encoding='utf8') as fr:
        data=json.load(fr)
        return data

def read_excel():
    df=pd.read_excel(os.path.join(settings.DB_PATH,'goods.xlsx'),index_col=0,header=0)
    return df

def save_excel(df):
    df.to_excel(os.path.join(settings.DB_PATH, 'goods.xlsx'))
