import numpy as np
import requests
import pandas as pd
from datetime import datetime
from datetime import timezone


def translate_time(name_file):  # функция перевода времени из формата YYYY-MM-DDTHH-MM-SSZ -> YYYY-MM-DD HH:MM:SS
    for i, v in enumerate(name_file.time):
        if v != 'UTC':
            d = datetime.fromisoformat(v[:-1]).astimezone(timezone.utc)
            name_file.time[i] = d.strftime('%Y-%m-%d %H:%M:%S')
    # a.to_csv('data.csv', mode='a', header=False)
    file_sort = name_file.sort_values(by=['fileNumber', 'time'])
    file_sort[:-1].to_csv('data.csv', mode='a', header=False)
    print("Recording is over")


def add_new_data(): # функция для скачивания данных с последней даты уже записанных данных
    df = pd.read_csv('data.csv')
    last_time = df.sort_values(by='time')[:-1]['time'].iloc[-1][:10]
    last_data = pd.read_csv(
        f"https://www.ifremer.fr/erddap/tabledap/ArgoFloats.csv?fileNumber%2Ctime%2Clatitude%2Clongitude%2Cpres%2Ctemp"
        f"%2Cpsal&time%3E={last_time}&latitude%3E=70&latitude%3C=90&longitude%3E=30&longitude%3C=60")
    print(last_time)
    return last_data


# add_new_data()
# translate_time(f)
