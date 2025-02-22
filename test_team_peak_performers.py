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

        # positive test case
        prefix = '123'
        middle = '456'
        suffix = '7890'
        test_str = prefix + '-' + middle + '-' + suffix
        result = analyze_text(test_str, ['PHONE_NUMBER'])

     # negative test case
        # too long
        test_str = '123-456-78999'
        result = analyze_text(test_str, ['PHONE_NUMBER'])


if __name__ == '__main__':
    unittest.main()
