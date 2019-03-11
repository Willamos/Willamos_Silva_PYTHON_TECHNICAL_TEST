from src.QuestionB.QuestionB import check_version

import unittest

class TestCheckVersion(unittest.TestCase):

    # case where left zeros can make a difference - the int value should be considered
    def test_01(self):
        version1 = '1.001.4.5.12'
        version2 = '1.01.3'
        expected_message = version2 + ' is older than ' + version1
        returned_messsage = check_version(version1, version2)
        self.assertEqual(expected_message, returned_messsage)

    # case where they should be equal
    def test_02(self):
        version1 = '1.001.4.5.12'
        version2 = '1.01.04.05.12'
        expected_message = 'both ' + version2 + ' and ' + version1 + ' are the same version'
        returned_messsage = check_version(version1, version2)
        self.assertEqual(expected_message, returned_messsage)

    # case where they should be different (2 older than 1)
    def test_03(self):
        version1 = '1.001.4.5.12'
        version2 = '1.01.03'
        expected_message = version2 + ' is older than ' + version1
        returned_messsage = check_version(version1, version2)
        self.assertEqual(expected_message, returned_messsage)

    # case to validate the last elif from the for loop (same version if comparing only same amount of items)
    def test_04(self):
        version1 = '1.01.03.0.0.1'
        version2 = '1.01.03'
        expected_message = version2 + ' is older than ' + version1
        returned_messsage = check_version(version1, version2)
        self.assertEqual(expected_message, returned_messsage)
        version3 = '1.01.03.0.0.0'
        version4 = '1.01.03'
        expected_message = 'both ' + version3+ ' and ' + version4 + ' are the same version'
        returned_messsage = check_version(version3, version4)
        self.assertEqual(expected_message, returned_messsage)


if __name__ == '__main__':
    unittest.main(verbosity=True)


