"""Unit test file for team tech_titans"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_tech_titans(unittest.TestCase):
    """Test team tech_titans PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

        
    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""
        # positive test case
        test_str = "12345678"
        result = analyze_text(test_str, ['US_DRIVER_LICENSE'])
        print(result)

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
