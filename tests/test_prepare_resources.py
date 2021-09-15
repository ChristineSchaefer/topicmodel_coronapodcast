import unittest

from prepare_resources.text_processing import remove_non_character, question_detection


class TestPrepareResources(unittest.TestCase):
    def test_remove_non_character(self):
        input = [' Was halten Sie davon?', '12345', ' [ Wie sehen Sie das? ]', '']
        output = ['Was halten Sie davon?', '12345', 'Wie sehen Sie das?']

        self.assertEqual(remove_non_character(input), output)

    def test_find_questions(self):
        input = ['Was halten Sie davon? Haben Sie Spaß? Wie sehen Sie das?', 'Kann ich Ihnen helfen? Ihre Meinung?']
        output = ['Was halten Sie davon?', 'Haben Sie Spaß?', 'Wie sehen Sie das?', 'Kann ich Ihnen helfen?',
                  'Ihre Meinung?']

        self.assertEqual(question_detection(input), output)
