import re

from nltk import RegexpTokenizer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import ngrams
import spacy as spacy

nlp = spacy.load("de_core_news_sm")


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
    for stopword in german_stopwords:
        if questions.__contains__(stopword):
            questions.remove(stopword)
    return questions


def tokenize_lemmatize(questions: list):
    tokens = list()
    lemmas = list()

    for q in questions:
        sentence = nlp(q)
        pre_token = list()
        pre_lemma = list()
        for token in sentence:
            if len(token.text) > 1 and not token.text.isnumeric():
                pre_token.append(token.text.lower())
                pre_lemma.append(token.lemma_.lower())
        tokens.append(pre_token)
        lemmas.append(pre_lemma)

    return tokens, lemmas

# TODO
def gen_ngrams(lemmas: list, size: int) -> list:
    ngrams = list()
    for lemma in lemmas:
        ngrams_store = list()
        onestring = ' '.join(lemma)
        ngram = ngrams(onestring, size)
        ngrams_store.append(ngram)
    ngrams.extend(ngrams_store)
    return ngrams