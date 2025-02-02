"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
        # positive test case
        prefix = '123'
        middle = '12'
        suffix = '1234'
        test_str = prefix + '-' + middle + '-' + suffix
        result = analyze_text(test_str, ['US_SSN'])
        # expect a result
        self.assertGreater(len(result), 0, 'Result is empty')
        # check correct entity_type
        self.assertEqual(result[0].entity_type, 'US_SSN')
        # check the score
        self.assertEqual(result[0].score, 0.5)

        # context enhancement
        # add context word
        test_str = 'ssn ' + test_str
        result = analyze_text(test_str, ['US_SSN'])
        # expect a result
        self.assertGreater(len(result), 0, 'Result is empty')
        # check correct entity_type
        self.assertEqual(result[0].entity_type, 'US_SSN')
        # check the score
        self.assertEqual(result[0].score, 0.85)

        # negative test case
        # too short
        test_str = '123-45-67'
        result = analyze_text(test_str, ['US_SSN'])
        # expect an empty list
        self.assertEqual(len(result), 0)



if __name__ == '__main__':
    unittest.main()
