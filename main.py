# Step 1: Load data from csv-file. Goal: list of questions, separated by asked scientist
from prepare_resources import questions_d, questions_c
from prepare_resources.text_processing import remove_stopwords

drosten_questions = questions_d
ciesek_questions = questions_c

# Step 2: Remove stopwords.
drosten_questions = remove_stopwords(drosten_questions)
ciesek_questions = remove_stopwords(ciesek_questions)

print(ciesek_questions)