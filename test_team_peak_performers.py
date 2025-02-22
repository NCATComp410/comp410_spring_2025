"""Unit test file for team peak_performers"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_peak_performers(unittest.TestCase):
    """Test team peak_performers PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""

    def test_location(self):
        """Test LOCATION functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""

        # negative test case
        #first 2 letters are not allowed as prefixes for NINO, last letter is not allowed as suffix for NINO
        test_string2 = 'YN 27 61 51 P'
        result2 = analyze_text(test_string2, ['UK_NINO'])
        
        self.assertEqual(len(result2), 0)


if __name__ == '__main__':
    unittest.main()
