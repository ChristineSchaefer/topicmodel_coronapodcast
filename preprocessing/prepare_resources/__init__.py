import csv

from preprocessing.prepare_resources.text_processing import remove_non_character, question_detection

# initialize variables
drosten_questions = list()
ciesek_questions = list()

# path to csv
path = 'podcast.csv'

with open(path, newline='', encoding='utf-8') as csvfile:
    podcast_reader = csv.reader(csvfile)
    # read each row from csv and write questions to list
    for row in podcast_reader:
        if row.__contains__("CD"):
            drosten_questions.append(row[3:len(row) - 1])
        elif row.__contains__("SC"):
            ciesek_questions.append(row[3:len(row) - 1])

questions_c = list()
for questions_list in ciesek_questions:
    # split questions
    all_questions_in_one = ' '.join(questions_list)
    if all_questions_in_one is not None or not " ":
        questions_c.append(all_questions_in_one)

questions_d = list()
for questions_list in drosten_questions:
    # split questions
    all_questions_in_one = ' '.join(questions_list)
    if all_questions_in_one is not None or not " ":
        questions_d.append(all_questions_in_one)


questions_d = remove_non_character(questions_d)
questions_d = question_detection(questions_d)
questions_c = remove_non_character(questions_c)
questions_c = question_detection(questions_c)
