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

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""
        # positive test case
        # Detect a valid US passport number
        text = "My US passport number is 123456789."
        results = analyze_text(text=text, entity_list=["US_PASSPORT"])

        self.assertGreater(len(results), 0, "US Passport number should be detected.")
        # negtative test case
        # Ensure invalid numbers aren't detected
        text = "My passcode is 98765432."  # Only 8 digits (invalid)
        results = analyze_text(text=text, entity_list=["US_PASSPORT"])

        self.assertEqual(len(results), 0, "Invalid passport number should not be detected.")


        # context enhancement

if __name__ == '__main__':
    unittest.main()
