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

        # positive test case
        start = 'RSSMRA85'
        end = 'M01H501Z'
        test_string = ''.join([start,end])
        result = analyze_text(test_string, ['IT_FISCAL_CODE'])

        # result
        self.assertGreater(len(result), 0)
        # checking the correct entity_type
        self.assertEqual(result[0].entity_type, 'IT_FISCAL_CODE')
        # score checker
        self.assertEqual(result[0].score, 0.3)

        # enhancement
        test_string = 'cf' + test_string
        result = analyze_text(test_string, ['IT_FISCAL_CODE'])
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0].entity_type, 'IT_FISCAL_CODE')
        self.assertEqual(result[0].score, 0.6499999999999999)

        # negative test case
        test_string2 = 'XBCDFR12A34Z567X'
        result2 = analyze_text(test_string2, ['IT_FISCAL_CODE'])

        # most likely an empty list
        self.assertEqual(len(result2), 0)


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
       
       # negative test case
        
        # context enhancement

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
