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

        #positive case
        test_str = '1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71'
        result = analyze_text(test_str, ['CRYPTO'])

        #expect a result
        self.assertGreater(len(result), 0, 'Result is empty')

        #check correct entity_type
        self.assertEqual(result[0].entity_type, 'CRYPTO')
        
        #negative case
        test_str = '2234567'
        result = analyze_text(test_str, ['CRYPTO'])
        # expect an empty list
        self.assertEqual(len(result), 0)
        #context enhancement

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
