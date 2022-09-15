from utils import *
from textrank_word import TextRank
from getHotWords import *
from HotWordMining import *

cases = readJson('/home/liangpan/visualization/ky/projects/热词分析/HotWordsMining/propressedData.json')
# cases=format_time(cases)#把字符串转为日期格式
# stop_words = get_stop_words('/home/liangpan/visualization/ky/projects/热词分析/HotWordsMining/stopWords.txt')
# cases = remove_stop_words_and_verbs(cases, stop_words)
# history_words = []
# current_words = []
# histoty_list = []
# current_list = []
# extract_tags = TextRank().textrank
# for case in cases:
#     lb=case['内容分类']
#     time1 = case['信访日期'][5:7]
#     if time1 == '07':
#         histoty_list.append(case)
#         history_words.append(extract_tags(case['概况']['tok/fine']))
#     if time1 == '08':
#         current_list.append(case)
#         current_words.append(extract_tags(case['概况']['tok/fine']))
# history_hot_words=get_hot_words(history_words)
# current_hot_words=get_hot_words(current_words)
words = get_hot_words(cases)
print(cases)
