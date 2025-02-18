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
        # positive test case
        prefix= 'AA'
        suffix= '1234567'
        test_str = ' '.join((prefix,suffix))
        results = analyze_text(test_str,["IT_IDENTITY_CARD"]) 
        # expect a result
        self.assertGreater(len(results),0, "Result Is Empty")
        # check correct entity_type
        self.assertEqual(results[0].entity_type,"IT_IDENTITY_CARD" )
        #check score
        self.assertEqual(results[0].score, 0.01)
        # context enhancement
        # add context words
        test_str += 'documento'
        test_str += 'carta'
        test_str += 'identità'
        test_str += 'elettronica'
        test_str += 'cie'
        test_str += 'documento'
        test_str += 'riconoscimento'
        test_str += 'espatrio'
        # expect a result
        self.assertGreater(len(results),0, "Result Is Empty")
        # check correct entity_type
        self.assertEqual(results[0].entity_type,"IT_IDENTITY_CARD" )
        #check score
        self.assertEqual(results[0].score, 0.01)
       # negative test case
        test_str = '23ad67888'
        results = analyze_text(test_str,["IT_IDENTITY_CARD"]) 
        #expect empty list
        self.assertEqual(len(results),0, "Result Is Empty")
        # New comment for new pull request
    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
