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

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""
        # positive test case
        test_str = '17893729974'
        result = analyze_text(test_str,['IT_VAT_CODE'])
        #expect a result
        self.assertGreater(len(result),0,'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'IT_VAT_CODE')
        #check the score
        self.assertEqual(result[0].score,0.5)

        # context enhancement
        # add context word
        test_str = test_str + 'iva'
        result = analyze_text(test_str,['IT_VAT_CODE'])
        #expect a result
        self.assertEqual(len(result),0,'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'IT_VAT_CODE')
        #check the score
        self.assertEqual(result[0].score,0.05)


        # negative test case
        #invalid vat number
        test_str = '00000000000'
        result = analyze_text(test_str,['IT_VAT_CODE'])
        # expect an empty list
        self.assertEqual(len(result),0)
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'IT_VAT_CODE')
        #check the score
        self.assertEqual(result[0].score,0.05)


        

if __name__ == '__main__':
    unittest.main()
