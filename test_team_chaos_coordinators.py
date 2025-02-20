"""Unit test file for team chaos_coordinators"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_chaos_coordinators(unittest.TestCase):
    """Test team chaos_coordinators PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""
        # positive Test case
        prefix = '01'
        middle = '01'
        suffix = '2000'
        test_str = prefix + '/' + middle + '/' + suffix
        result = analyze_text(test_str,['DATE_TIME'] )
        # expect result
        self.assertGreater(len(result), 0, 'Result empty')
        # check correct entity_type
        self.assertEqual(result[0].entity_type, 'DATE_TIME')
        # check the score
        self.assertEqual(result[0].score, 0.6)

        #context enhancement
        # add context word
        test_str += 'birthday'
        result = analyze_text(test_str, ['DATE_TIME'])
        # expect a result
        self.assertGreater(len(result), 0, 'Result is Empty')
        # check correct entity_type
        self.assertEqual(result[0].entity_type, 'DATE_TIME')
        # check the score
        self.assertEqual(result[0].score, 0.44999999999999996)
        # negative test case
        # too short
        test_str = '1-01-2000'
        result = analyze_text(test_str, ['DATE_TIME'])
        # expect empty list
        self.assertEqual(len(result), 1)
    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
