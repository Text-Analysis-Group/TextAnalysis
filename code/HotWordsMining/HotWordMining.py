# from math import *
from collections import OrderedDict

from collections import Counter

from gensim import corpora
from gensim.models import TfidfModel


# def compute_word_info(history_text, current_text):
#     """
#     为每个词计算历史词频、当前词频、总词频(历史词频+当前词频)、总词频率(当前词频/总词频)
#     :param history_text: 历史文本
#     :param current_text: 当前文本
#     :return: word_info: Dict: 每个词的历史词频,当前词频,总词频和总词频率
#              num_count_avg: Float： 所有词总词频均值: (W1(总词频) + W2(总词频) +...+WN(总词频)) / N
#              rate_count_avg: Flaot: 所有词总词频率均值: (W1(总词频率) + W2(总词频率) +...+WN(总词频率)) / N
#     """
#     word_info = dict()
#     # 计算历史词频
#     for word in history_text:
#         if not (word in word_info.keys()):
#             word_info[word] = {"history_num": 1, "current_num": 0}
#         else:
#             word_info[word]["history_num"] += 1
#     # 计算当前词频
#     for word in current_text:
#         if not (word in word_info.keys()):
#             word_info[word] = {"history_num": 0, "current_num": 1}
#         else:
#             word_info[word]["current_num"] += 1
#     num_count = 0
#     rate_count = 0
#     # 计算总词频和总词频率
#     for word in word_info:
#         word_info[word]["sum"] = word_info[word]["history_num"] + word_info[word]["current_num"]
#         word_info[word]["rate"] = word_info[word]['current_num'] / word_info[word]['sum']
#         num_count += word_info[word]['sum']
#         rate_count += word_info[word]['rate']
#     num_count_avg = num_count / len(word_info)
#     rate_count_avg = rate_count / len(word_info)
#     return word_info, num_count_avg, rate_count_avg
#
#
# def bayes_func(cur_sum, cur_rate, num_avg, rate_avg):
#     """
#     贝叶斯均值计算
#     :param cur_sum: 当前总词频
#     :param cur_rate: 当前总词频率
#     :param num_avg: 所有词总词频均值
#     :param rate_avg: 所有词总词频率均值
#     :return:
#     """
#     return (cur_sum * cur_rate + num_avg * rate_avg) / (cur_sum + num_avg + 1)
#
#
# def newton_func(cur_num, his_num, time_diff):
#     """
#     牛顿冷却系数计算
#     :param cur_num: int: 当前词频
#     :param his_num: int: 历史词频
#     :param time_diff: int: 时间差
#     :return:
#     """
#     return log((cur_num + 1) / (his_num + 1), e) / time_diff
#
#
# def bn_hot(history_text, current_text):
#     """
#     词热度值计算: Hot = 0.7 * bayes_func + 0.3 * newton_func
#     :param words: 词列表
#     :param history_text: 历史文本
#     :param current_text: 当前文本
#     :return: Dict: {
#         word: hot_value
#     }
#     已按热度值降序排序
#     """
#     bn_word_hot_map = dict()
#     word_info, num_count_avg, rate_count_avg = compute_word_info(history_text, current_text)
#     for word in word_info:
#         bn_word_hot_map[word] = 0.7 * bayes_func(word_info[word]['sum'],
#                                                  word_info[word]['rate'],
#                                                  num_count_avg,
#                                                  rate_count_avg) + \
#                                 0.3 * newton_func(word_info[word]['current_num'],
#                                                   word_info[word]['history_num'],
#                                                   7)
#     sortDict = sorted(bn_word_hot_map.items(), key=lambda x: x[1], reverse=True)
#     return OrderedDict(sortDict)


def word_rates(words):
    count = Counter(words)
    dictionary = dict(count)
    return count.most_common(20)
def compute_tfidf(texts):
    dictionary = corpora.Dictionary(texts)
    id2words = dict(zip(dictionary.token2id.values(), dictionary.token2id.keys()))
    corpus = [dictionary.doc2bow(text) for text in texts]
    tf_idf_model = TfidfModel(corpus, normalize=False)
    texts_id_tf_idf = [tf_idf_model[doc] for doc in corpus]
    texts_tf_idf = []
    high_tf_idf = {}
    for text_id_tf_idf in texts_id_tf_idf:
        temp = sorted(text_id_tf_idf, key=lambda x: x[1], reverse=True)
        tf_idf = {}
        for value in temp:
            if id2words[value[0]] in high_tf_idf.keys():
                high_tf_idf[id2words[value[0]]] = high_tf_idf[id2words[value[0]]] + value[1]
            else:
                high_tf_idf[id2words[value[0]]] = value[1]
            tf_idf[id2words[value[0]]] = value[1]
        texts_tf_idf.append(tf_idf)
    high_tf_idf = sorted(high_tf_idf.items(), key=lambda d: d[1], reverse=True)
    return texts_tf_idf, high_tf_idf


def all_td_idf(cases):
    texts = []
    for case in cases:
        texts.append(case['概况']['tok/fine'])
    return compute_tfidf(texts)
