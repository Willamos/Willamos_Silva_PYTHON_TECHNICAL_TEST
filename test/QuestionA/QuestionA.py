from src.QuestionA.QuestionA import do_they_overlap
import unittest

class TestCheckVersion(unittest.TestCase):
    def test_01(self):
        x = (2, 5)
        y = (3, 6)
        self.assertTrue(do_they_overlap(x, y))

    def test_02(self):
        x = (2, 5)
        y = (5.1, 6)
        self.assertFalse(do_they_overlap(x, y))

    def test_03(self):
        x = (2, 5)
        y = (0, 1)
        self.assertFalse(do_they_overlap(x, y))

    def test_04(self):
        x = (2, 5)
        y = (1, 2.1)
        self.assertTrue(do_they_overlap(x, y))



if __name__ == '__main__':
    unittest.main(verbosity=True)

