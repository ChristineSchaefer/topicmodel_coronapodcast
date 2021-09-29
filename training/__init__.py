# ##imports
from gensim.models import LdaModel
from pprint import pprint


# ##functions
def train_lda(dictionary, corpus) -> None:
    """Function to set LDA Model from Gensim and train it. Compute for each question 5 topics.

            Parameters:
            ----------
                dictionary: Dictionary
                    Receives a dictionary representation from data.
                corpus: list
                    Receives a bow representation from corpus"""

    # Set training parameters.
    num_topics = 5      # number of topics
    chunksize = 2000    # number of processed documents at a time
    passes = 20         # how often the model will be trained
    iterations = 400    # how often a particular loop will be repeated over each document
    eval_every = 1      # evaluate each iteration

    # make a index to word dictionary.
    temp = dictionary[0]    # "load" the dictionary.
    id2word = dictionary.id2token

    # set model parameters
    model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        chunksize=chunksize,
        alpha='auto',
        eta='auto',
        iterations=iterations,
        num_topics=num_topics,
        passes=passes,
        eval_every=eval_every
    )

    # generate top topics
    top_topics = model.top_topics(corpus)  # , num_words=20)

    # Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    pprint(top_topics)
