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
        #positive test case
        prefix = 'n'
        middle = 'h'
        suffix = 's'
        test_str = (prefix + middle + suffix).lower()
        result = analyze_text(test_str,['UK_NHS'])
        #expect a result
        self.assertGreater(len(result), 0, 'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'UK_NHS')

        #negative test case

        #context enhancement
    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
