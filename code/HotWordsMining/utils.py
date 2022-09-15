import json
import time
import csv
from gensim import models
from gensim import corpora
from gensim.models import TfidfModel
import hanlp
import pandas as pd

hanlp.pretrained.mtl.ALL
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)


# 分词
def part(cases: list(dict())):
    pos = HanLP['pos/pku']
    tok = HanLP['tok/fine']
    tok_coarse = HanLP['tok/coarse']
    dictionary = getDict('pos_pku.csv')
    pos.dict_tags = dictionary

    tok.dict_combine = dictionary.keys()
    tok_coarse.dict_combine = dictionary.keys()
    i = 0
    for case in cases:
        print(str(i) + ' ' + str(len(cases)))
        content=case['概况']
        case["概况"] = HanLP(content, tasks='pos*')
        case['概况']['tok/coarse'] = HanLP(content, tasks='tok/coarse')['tok/coarse']

        i += 1
    return cases


def getDict(path):
    '''
    获取自定义词典
    :param path:
    :return:
    '''
    with open(path, mode='r') as f:
        reader = csv.reader(f)
        dictionary = {row[0]: row[1] for row in reader}
    return dictionary


def get_stop_words(stop_word_path):
    stop_words = list()
    with open(stop_word_path, 'r') as f:
        for line in f:
            stop_words.append(list(line.strip('\n').split(','))[0])
    return stop_words


def remove_stop_words_and_verbs(cases, stop_words, remove_verb=True):
    '''
    去除停用词和动词等，留下名词
    :param cases:
    :param stop_words:
    :return:
    '''
    for case in cases:
        temp = []
        for i in range(len(case['概况']['tok/fine'])):
            word = case['概况']['tok/fine'][i]
            pos = case['概况']['pos/pku'][i]
            if word in stop_words:
                continue
            if remove_verb == True and not is_noun(pos):
                continue
            temp.append(word)
        case['概况']['tok/fine'] = temp
    return cases


def is_noun(pos):
    poses = ['vn', 's', 'r', 'Rg', 'nz', 'nx', 'nt', 'ns', 'nr', 'n', 'Ng', 'l', 'i', 'an', 'ad']
    return pos in poses


def readFileData(path):
    '''
    读取excel文件
    :param path:
    :return:
    '''
    data = pd.read_excel(path)
    head_list = list(data.columns)
    data_list = []
    for i in data.values:
        row = dict(zip(head_list, i))
        data_list.append(row)
    print(data)
    return data_list


def readJson(path):
    with open(path, 'r', encoding='utf8') as f:
        cases = json.load(f)
    return cases


def format_time(cases):
    for case in cases:
        case['信访日期'] = time.strptime(case['信访日期'], '%Y-%m-%d')
