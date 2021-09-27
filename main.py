import logging
import sys

from preprocessing import initialize_corpora, get_lemmas, get_tokens
from training import train_lda
from gensim.corpora import Dictionary
from timeit import default_timer as timer
from datetime import timedelta

logging.basicConfig(filename='lda.log',
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    filemode='w',
                    level=logging.INFO)


def start_lda():
    initialize_corpora()

    logging.info(f'\n\n**************TOPIC MODELING SANDRA CIESEK**************')
    # Step 5: Compute bow-representation of data.
    ciesek_dict = Dictionary(get_lemmas('SC'))
    # Filter out words that occur less than 20 documents, or more than 50% of the documents.
    ciesek_dict.filter_extremes(no_below=20, no_above=0.5)
    # Bag-of-words representation of the documents.
    c_corpus = [ciesek_dict.doc2bow(question) for question in get_lemmas('SC')]

    print('Number of unique tokens: %d' % len(ciesek_dict))
    print('Number of documents: %d' % len(c_corpus))

    train_lda(ciesek_dict, c_corpus)

    logging.info(f'\n\n**************TOPIC MODELING CHRISTIAN DROSTEN**************')
    drosten_dict = Dictionary(get_lemmas('CD'))
    drosten_dict.filter_extremes(no_below=20, no_above=0.5)
    d_corpus = [drosten_dict.doc2bow(question) for question in get_lemmas('CD')]

    print('Number of unique tokens: %d' % len(drosten_dict))
    print('Number of documents: %d' % len(d_corpus))

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
