import xlrd
import pandas as pd


def readFileData(path):
    data = pd.read_excel(path)
    head_list = list(data.columns)
    data_list = []
    for i in data.values:
        row = dict(zip(head_list, i))
        data_list.append(row)
    print(data)
    return data_list
