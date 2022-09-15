from textrank_word import TextRank
from HotWordMining import *
from utils import *


def get_hot_words(cases, remove_verb=True):
    stop_words = get_stop_words('stopWords.txt')
    cases = remove_stop_words_and_verbs(cases, stop_words, remove_verb)
    extract_tags = TextRank().textrank
    keywords = []
    for content in cases:
        keywords.extend(extract_tags(content['概况']['tok/fine']))
    word_rate = word_rates(keywords)
    return word_rate
