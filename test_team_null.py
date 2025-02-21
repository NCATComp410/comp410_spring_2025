"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""
        # positive test case
        prefix = '123'
        middle = '456'
        suffix = '7890'
        test_str = prefix + '-' + middle + '-' + suffix
        result = analyze_text(test_str, ['PHONE_NUMBER'])
        # expect a result
        self.assertGreater(len(result), 0, 'Result is empty')
        # check correct entity_type
        self.assertEqual(result[0].entity_type, 'PHONE_NUMBER')
        # check the score
        self.assertEqual(result[0].score, 0.5)

        # context enhancement
        # add context word
        test_str = 'phone_number ' + test_str
        result = analyze_text(test_str, ['PHONE_NUMBER'])
        # expect a result
        self.assertGreater(len(result), 0, 'Result is empty')
        # check correct entity_type
        self.assertEqual(result[0].entity_type, 'PHONE_NUMBER')
        # check the score
        self.assertEqual(result[0].score, 0.85)

        # negative test case
        # too short
        test_str = '123-456-789'
        result = analyze_text(test_str, ['PHONE_NUMBER'])
        # expect an empty list
        self.assertEqual(len(result), 0)



if __name__ == '__main__':
    unittest.main()
