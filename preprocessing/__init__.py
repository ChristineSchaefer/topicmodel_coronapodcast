from preprocessing.helper import merge_lists
from preprocessing.prepare_resources import questions_d, questions_c
from preprocessing.prepare_resources.text_processing import remove_stopwords, gen_ngrams, tokenize, lemmatizer

ciesek_lemma = list()
drosten_lemma = list()
ciesek_token = list()
drosten_token = list()


def initialize_corpora() -> None:
    global ciesek_lemma, drosten_lemma, ciesek_token, drosten_token

    # Step 1: Load data from csv-file. Goal: list of questions, separated by asked scientist
    drosten_questions = questions_d
    ciesek_questions = questions_c

    # Step 2: Remove stopwords.
    drosten_questions = remove_stopwords(drosten_questions)
    ciesek_questions = remove_stopwords(ciesek_questions)

    # Step 3: Tokenize and lemmatize list with questions.
    ciesek_token = tokenize(ciesek_questions)
    ciesek_lemma = lemmatizer(ciesek_questions)
    drosten_token = tokenize(drosten_questions)
    drosten_lemma = lemmatizer(drosten_questions)

    # Step 4: Compute bigrams and trigrams.
    ciesek_bigrams = gen_ngrams(ciesek_lemma, 2)
    ciesek_trigrams = gen_ngrams(ciesek_lemma, 3)
    drosten_bigrams = gen_ngrams(drosten_lemma, 2)
    drosten_trigrams = gen_ngrams(drosten_lemma, 3)

    # add bigrams and trigrams to list
    c_words = merge_lists(ciesek_lemma, ciesek_bigrams, ciesek_trigrams)
    d_words = merge_lists(drosten_lemma, drosten_bigrams, drosten_trigrams)


def get_lemmas(scientist: str) -> list:
    if scientist == 'CD':
        return drosten_lemma
    elif scientist == 'SC':
        return ciesek_lemma


def get_tokens(scientist: str) -> list:
    if scientist == 'CD':
        return drosten_token
    elif scientist == 'SC':
        return ciesek_token
