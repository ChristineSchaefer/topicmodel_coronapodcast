import re

import nltk
from nltk.corpus import stopwords
from nltk import ngrams
import spacy as spacy

from preprocessing.helper import read_txt_file

nlp = spacy.load("de_core_news_sm")


# remove non character from list
def remove_non_character(questions: list) -> list:
    q = list()
    for question_list in questions:
        question_list = question_list.replace('[', '').replace(']', '').replace('\xad', '')
        re.sub(r'\W', '', question_list)
        if question_list:
            q.append(question_list.strip())
    return q


def question_detection(questions: list) -> list:
    list_question = list()
    for item in questions:
        q = nlp(item)
        for question in q.sents:
            if question or not ' ':
                list_question.append(str(question).strip())
    return list_question


def remove_stopwords(questions: list) -> list:
    german_stopwords = stopwords.words('german')
    extern_stopwords = read_txt_file('stopwords.txt')
    for sw in german_stopwords:
        if questions.__contains__(sw):
            questions.remove(sw)
    for sw in extern_stopwords:
        if questions.__contains__(sw):
            questions.remove(sw)
    return questions


def tokenize(questions: list) -> list:
    tokens = list()

    for q in questions:
        sentence = nlp(q)
        pre_token = list()
        for token in sentence:
            if len(token.text) > 1 and not token.text.isnumeric():
                pre_token.append(token.text.lower())
        tokens.append(pre_token)

    return tokens


def lemmatizer(questions: list) -> list:
    lemmas = list()

    for q in questions:
        sentence = nlp(q)
        pre_lemma = list()
        for token in sentence:
            if len(token.text) > 1 and not token.text.isnumeric():
                pre_lemma.append(token.lemma_.lower())
        lemmas.append(pre_lemma)

    return lemmas


def gen_ngrams(sentences: list, size: int) -> list:
    unigrams = []
    ngram = []
    for word in sentences:
        unigrams.append(word)
        ngram.extend(list(ngrams(word, size)))

    ngram = remove_stopwords(ngram)
    freq_ngram = nltk.FreqDist(ngram)
    # print(f'Most common {size}-grams: ', freq_ngram.most_common(20))

    for n in ngram:
        if not freq_ngram.most_common(20).__contains__(n):
            ngram.remove(n)

    return ngram
