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
        #positive test case
        prefix = '4111'
        middleOne = '1111'
        middleTwo = '1111'
        suffix = '1111'
        test_str = '-'.join([prefix, middleOne, middleTwo, suffix])
        result = analyze_text(test_str, ['CREDIT_CARD'])
        #expect a result
        self.assertIsNotNone(result)
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'CREDIT_CARD')

        #negative test case
        test_str = '1234 5678 9101 1121'
        result = analyze_text(test_str, ['CREDIT_CARD'])
        #expect an empty list
        self.assertEqual(len(result), 0)

        #context enhancement
        
    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
