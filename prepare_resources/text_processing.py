import re
from nltk.corpus import stopwords
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
