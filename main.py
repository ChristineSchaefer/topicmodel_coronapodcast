""" MAIN SCRIPT of the application. Manages the main components of the tool."""

# ##imports
import logging
import sys

from preprocessing import initialize_corpus, get_lemmas, get_tokens
from training import train_lda
from gensim.corpora import Dictionary
from timeit import default_timer as timer
from datetime import timedelta

# configuration logging
logging.basicConfig(filename='docs/lda.log',
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    filemode='w',
                    level=logging.INFO)


# ##functions
def start_lda():

    # Step 1: Load corpus: csv file with questions asked in podcasts
    initialize_corpus()

# ---------- LDA Sandra Ciesek ---------------

    # Step 2: Create dictionaries and bow representations for scientist. Use gensim.
    logging.info(f'\n\n**************TOPIC MODELING SANDRA CIESEK**************')

    # compute dictionary representation of data
    # mapping between the questions and ids
    ciesek_dict = Dictionary(get_lemmas('SC'))
    # print mapping
    print(ciesek_dict.token2id)
    print(len(ciesek_dict))
    # filter out words that occur less than 5 documents, or more than 50% of the documents
    # change values for larger corpora
    ciesek_dict.filter_extremes(no_below=5, no_above=0.5)
    # bag-of-words representation of the documents
    c_corpus = [ciesek_dict.doc2bow(question) for question in get_lemmas('SC')]
    print(c_corpus)

    print('Number of unique tokens: %d' % len(ciesek_dict))
    print('Number of documents: %d' % len(c_corpus))

    # Step 3: Train LDA-Model. Use gensim.
    train_lda(ciesek_dict, c_corpus)

# ---------- LDA Christian Drosten ---------------

    # Step 2: Create dictionaries and bow representations for scientist. Use gensim.
    logging.info(f'\n\n**************TOPIC MODELING CHRISTIAN DROSTEN**************')

    # compute dictionary representation of data
    drosten_dict = Dictionary(get_lemmas('CD'))
    # print mapping
    print(drosten_dict.token2id)
    print(len(drosten_dict))
    # filter out words that occur less than 5 documents, or more than 50% of the documents
    # change values for larger corpora
    drosten_dict.filter_extremes(no_below=5, no_above=0.5)
    # bag-of-words representation of the documents
    d_corpus = [drosten_dict.doc2bow(question) for question in get_lemmas('CD')]
    print(d_corpus)

    print('Number of unique tokens: %d' % len(drosten_dict))
    print('Number of documents: %d' % len(d_corpus))

    # Step 3: Train LDA-Model. Use gensim.
    train_lda(drosten_dict, d_corpus)


if __name__ == '__main__':
    # start timer
    start = timer()
    # set first logging/printing
    logging.info('\n\n******************************** The program started. ********************************\n')
    print('\n\n******************************** The program started. ********************************\n')

    start_lda()

    # set final logging/printing
    logging.info(
        '\n\n******************************** The program finished. ********************************\n')
    print('Processing done. For further information see logger-files.')
    print('\n\n******************************** The program finished. ********************************\n')
    # finish timer
    end = timer()
    print(f'Runtime of program: {timedelta(seconds=end - start)}.')
    sys.exit()
