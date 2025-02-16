"""Unit test file for team not_like_us"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_not_like_us(unittest.TestCase):
    """Test team not_like_us PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""
        # Will Walton: Positive Test Case Refinements
        prefix = "BA"
        numbers = "1234567"
        suffix = "Z"

        license_num = prefix + numbers + suffix #Build Valid Format
        test_string = f"License number: {license_num}"
        result = analyze_text(test_string, ["IT_DRIVER_LICENSE"])

        #Unittest to check that it found something
        self.assertTrue(len(result)>0, "Result is empty - license not detected")
        self.assertEqual(result[0].entity_type, "IT_DRIVER_LICENSE")

       #Negative Test Case
        invalid_license = "123456789"
        result = analyze_text(invalid_license, ["IT_DRIVER_LICENSE"])

        # make sure entity is not detected
        self.assertEqual(len(result),0)
        

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
