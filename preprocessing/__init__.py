# ## imports
from preprocessing.helper import merge_lists
from preprocessing.prepare_resources import get_question_list
from preprocessing.prepare_resources.text_processing import remove_stopwords, gen_ngrams, tokenize, lemmatizer

# set variables
ciesek_lemma = list()
drosten_lemma = list()
ciesek_token = list()
drosten_token = list()


# ##functions
def initialize_corpus() -> None:
    """Function to start loading and processing corpus of questions asked in podcasts.
        Fill needed lists with tokens and lemmas for topic modelling.
        Lists are separated by scientists Sandra Ciesek and Christian Drosten."""

    # set globals
    global ciesek_lemma, drosten_lemma, ciesek_token, drosten_token

    # Step 1: Load data from csv-file. Goal: list of questions, separated by asked scientist
    drosten_questions = get_question_list('CD')
    ciesek_questions = get_question_list('SC')

    # Step 2: Remove stopwords.
    drosten_questions = remove_stopwords(drosten_questions)
    ciesek_questions = remove_stopwords(ciesek_questions)

    # Step 3: Tokenize and lemmatize list with questions.
    ciesek_token = tokenize(ciesek_questions)
    ciesek_lemma = lemmatizer(ciesek_questions)
    drosten_token = tokenize(drosten_questions)
    drosten_lemma = lemmatizer(drosten_questions)

# ----- not necessary part for lda -------
    # follow description on:
    # https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html#sphx-glr-auto-examples-tutorials-run-lda-py

    # Step 4: Compute bigrams and trigrams.
    ciesek_bigrams = gen_ngrams(ciesek_lemma, 2)
    ciesek_trigrams = gen_ngrams(ciesek_lemma, 3)
    drosten_bigrams = gen_ngrams(drosten_lemma, 2)
    drosten_trigrams = gen_ngrams(drosten_lemma, 3)

    # add bigrams and trigrams to list
    c_words = merge_lists(ciesek_lemma, ciesek_bigrams, ciesek_trigrams)
    d_words = merge_lists(drosten_lemma, drosten_bigrams, drosten_trigrams)

# ----- end -----


def get_lemmas(scientist: str) -> list:
    """Function to return list of lemmas for asked scientist.

            Parameters:
            -----------
                scientist: str
                    Receives shortcut for scientist (SC or CD).

            Returns:
            --------
                list of lemma"""

    if scientist == 'CD':
        return drosten_lemma
    elif scientist == 'SC':
        return ciesek_lemma


def get_tokens(scientist: str) -> list:
    """Function to return list of token for asked scientist.

                Parameters:
                -----------
                    scientist: str
                        Receives shortcut for scientist (SC or CD).

                Returns:
                --------
                    list of token"""

    if scientist == 'CD':
        return drosten_token
    elif scientist == 'SC':
        return ciesek_token
