# Step 1: Load data from csv-file. Goal: list of questions, separated by asked scientist
from prepare_resources import questions_d, questions_c
from prepare_resources.text_processing import remove_stopwords, tokenize_lemmatize, gen_ngrams

drosten_questions = questions_d
ciesek_questions = questions_c

# Step 2: Remove stopwords.
drosten_questions = remove_stopwords(drosten_questions)
ciesek_questions = remove_stopwords(ciesek_questions)

# Step 3: Tokenize and lemmatize list with questions.
ciesek_token, ciesek_lemma = tokenize_lemmatize(ciesek_questions)
drosten_token, drosten_lemma = tokenize_lemmatize(drosten_questions)

# Step 4: Compute bigrams.
ciesek_bigrams = gen_ngrams(ciesek_lemma, 2)

# Step 5: Compute bow-representation of data.