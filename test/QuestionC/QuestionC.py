from src.QuestionC.QuestionC import *

import unittest

class TestScrapper(unittest.TestCase):
    scrapper = Scrapper()


    def test_count_occurencies_01(self):
        paragraph = 'the house is a very beautiful house, with big house windows'
        query = 'house'
        self.assertEqual(self.scrapper.count_occurences(paragraph, query), 3)

    def test_count_occurencies_02(self):
        paragraph = 'the house is a very beautiful house, with big house windows'
        query = 'beautiful'
        self.assertNotEqual(self.scrapper.count_occurences(paragraph, query), 3)


    def test_remove_stop_words(self):
        old_string = 'this is a very good house'
        new_string = self.scrapper.remove_stop_words(old_string)
        self.assertNotEqual(old_string, new_string, 'strings arent equal')
        self.assertEqual(new_string, 'good house')



if __name__ == '__main__':
    unittest.main(verbosity=True)

