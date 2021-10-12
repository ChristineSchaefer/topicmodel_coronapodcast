# ##imports
import csv
from preprocessing.prepare_resources.text_processing import remove_non_character, question_detection


# ##functions
def get_question_list(scientist: str) -> list:
    """Function to return list of questions for asked scientist.

            Parameters:
            -----------
                scientist: str
                    Receives shortcut for scientist (SC or CD).

            Returns:
            --------
                list of questions"""

    # set variables
    drosten_questions = list()
    ciesek_questions = list()
    number_interviews_d = 0
    number_interviews_c = 0
    path = 'podcast.csv'

    # initialize question list of scientists
    with open(path, newline='', encoding='utf-8') as csv_file:
        podcast_reader = csv.reader(csv_file)
        # read each row from csv and write questions to list
        for row in podcast_reader:
            if row.__contains__("CD"):
                # fill list with questions
                drosten_questions.append(row[3:len(row) - 1])
                number_interviews_d += 1
            elif row.__contains__("SC"):
                # fill list with questions
                ciesek_questions.append(row[3:len(row) - 1])
                number_interviews_c += 1

    if scientist == 'SC':
        ciesek_questions = __normalized_questions(ciesek_questions)
        print('Number of interviews with Ciesek: ', number_interviews_c)
        return ciesek_questions
    if scientist == 'CD':
        drosten_questions = __normalized_questions(drosten_questions)
        print('Number of interviews with Drosten: ', number_interviews_d)
        return drosten_questions
    else:
        # default
        print(f'No questions for {scientist} found.')


def __normalized_questions(questions: list) -> list:
    """Function to normalized loaded data from csv.

            Parameters:
            ----------
                questions: list
                    Receives a list with question asked for scientist.

            Returns:
            -------
                list with normalized questions"""

    normalized_questions = list()

    for q in questions:
        # there are more than one questions in one list element
        # all strings in one element will be join together and then can be separated again
        all_questions_in_one = ' '.join(q)
        if all_questions_in_one is not None or not " ":
            normalized_questions.append(all_questions_in_one)

    # remove remaining list elements in strings and detect single questions to store in list
    normalized_questions = remove_non_character(normalized_questions)
    normalized_questions = question_detection(normalized_questions)

    return normalized_questions
