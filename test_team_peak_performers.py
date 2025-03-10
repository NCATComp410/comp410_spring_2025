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
        # Positive Test Case: Detecting a Person entity
        name = 'John'
        middle_N = 'Elliot'
        last_Name = 'Doe'

        test_str = f"{name} {middle_N} {last_Name}"
        result = analyze_text(test_str, ['PERSON'])

        # Expect a result (non-empty list)
        self.assertGreater(len(result), 0, 'Result is empty')

        # Check if the detected entity type is correct
        self.assertEqual(result[0].entity_type, 'PERSON')

        # Check the confidence score
        self.assertEqual(result[0].score, 0.85)

        # Negative Test Case 
        test_str = 'error'
        result = analyze_text(test_str, ['PERSON'])

        # Expect no results (empty list)
        self.assertEqual(len(result), 0, 'Expected no entity detection')

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
