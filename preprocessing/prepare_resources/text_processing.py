# ##imports
import re
import nltk
from nltk.corpus import stopwords
from nltk import ngrams
import spacy as spacy

# load nlp model from spacy
nlp = spacy.load("de_core_news_sm")


# ##functions
def remove_non_character(questions: list) -> list:
    """Function to remove remaining list characters and non word character from string.

            Parameters:
            -----------
                questions: list
                    Receives a list with questions.

            Returns:
            -------
                list without non characters and list characters"""

    q = list()
    for question_list in questions:
        # remove remaining list characters
        question_list = question_list.replace('[', '').replace(']', '').replace('\xad', '')
        # remove non word character
        re.sub(r'\W', '', question_list)
        if question_list:
            q.append(question_list.strip())
    return q


def question_detection(questions: list) -> list:
    """Function to detect sentence boundaries and split strings into single ones. Here: only questions.

            Parameters:
            -----------
                questions: list
                    Receives a list with questions. Many questions can be in one string.

            Returns:
            -------
                list splitted into single questions"""

    list_question = list()
    for item in questions:
        # use spacy model to detect sentences
        q = nlp(item)
        for question in q.sents:
            if question or not ' ':
                list_question.append(str(question).strip())
    return list_question


def remove_stopwords(questions: list) -> list:
    """Function to remove stopwords.

            Parameters:
            ----------
                questions: list
                    Receives a list with questions. One list element is one question.

            Returns:
            -------
                list without stopwords"""

    # use nltk stopwords and compare them with questions
    german_stopwords = stopwords.words('german')
    for sw in german_stopwords:
        if questions.__contains__(sw):
            questions.remove(sw)
    return questions


def tokenize(questions: list) -> list:
    """Function to tokenize questions.

            Parameters:
            ----------
                questions: list
                    Receives a list with questions. One list element is one question.

            Returns:
            -------
                list of token"""

    tokens = list()

    for q in questions:
        # use spacy model to detect sentences and use token
        sentence = nlp(q)
        pre_token = list()
        for token in sentence:
            # only return tokens with pos tag 'NOUN'
            if len(token.text) > 1 and not token.text.isnumeric() and token.pos_ == 'NOUN':
                pre_token.append(token.text.lower())
        tokens.append(pre_token)
    for token in tokens:
        # remove empty strings
        if not token:
            tokens.remove(token)

    return tokens


def lemmatizer(questions: list) -> list:
    """Function to found lemmas from token.

            Parameters:
            ---------
                questions: list
                    Receives a list with questions. One list element is one question.

            Returns:
            -------
                list of lemmas"""

    lemmas = list()

    for q in questions:
        # use spacy model to detect sentences and use lemma
        sentence = nlp(q)
        pre_lemma = list()
        for token in sentence:
            # only return lemma with pos tag 'NOUN'
            if len(token.text) > 1 and not token.text.isnumeric() and token.pos_ == 'NOUN':
                pre_lemma.append(token.lemma_.lower().strip())
        lemmas.append(pre_lemma)
    for lemma in lemmas:
        # remove empty strings
        if not lemma:
            lemmas.remove(lemma)
    return lemmas


def gen_ngrams(sentences: list, size: int) -> list:
    """Function to generate n-grams.

            Parameters:
            ---------
                sentences: list
                    Receives a list with lemmas. One list element contains all lemmas from one question.
                size: int
                    Receive the size of n-gram.

            Returns:
            -------
                list of n-grams"""

    unigrams = []
    ngram = []
    for word in sentences:
        unigrams.append(word)
        # use ngrams from nltk
        ngram.extend(list(ngrams(word, size)))

    # remove unnecessary n-grams
    ngram = remove_stopwords(ngram)
    # compute frequency of n-grams
    freq_ngram = nltk.FreqDist(ngram)
    # print(f'Most common {size}-grams: ', freq_ngram.most_common(20))

    for n in ngram:
        # only keep n-grams that are most occur
        if not freq_ngram.most_common(20).__contains__(n):
            ngram.remove(n)
    return ngram
