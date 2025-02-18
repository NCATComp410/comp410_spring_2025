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
        
        invalid_licenes = ["123456789","ABC12345", "A1234567Z", "AB12345678",
         "AB12345", "AB 1234567 Z", "ab1234567z" "@XY1234567Z"]

        for invalid_license in invalid_licenes:
            result = analyze_text(invalid_license,["IT_DRIVER_LICENSE"])

            #make sure entity is not detected and prevents false negatives
            if len(result)>0:
                self.assertLessEqual(result[0].score,0.2, f"Detected invalid license: { invalid_license}-{result}")
        

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
         # positive test case
        prefix = 'AB'
        middle = '123'
        suffix = '4567'
        test_str = prefix + middle + suffix
        result = analyze_text(test_str, ['IT_PASSPORT'])
        #Expect a result
        self.assertGreater(len(result), 0, 'Result is empty')
        # Check correct entity type
        self.assertEqual(result[0].entity_type, "IT_PASSPORT")
        #Check the score
        self.assertGreaterEqual(result[0].score, 0.01)

        # context enhancement
        # add context work
        test_str = test_str + 'passaporto'
        result = analyze_text(test_str, ['IT_PASSPORT'])
        #Expect a result
        self.assertGreater(len(result), 0, 'Result is empty')

        # Check correct entity type
        self.assertEqual(result[0].entity_type, "IT_PASSPORT")

        #Check the score
        self.assertGreaterEqual(result[0].score, 0.01)


        # negative test case
        # too short
        test_str = 'AB12345'
        result = analyze_text(test_str, ['IT_PASSPORT'])
        # expect an empty list
        self.assertEqual(len(result), 0)

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""
        # positive test case
        test_str = '17893729974'
        result = analyze_text(test_str,['IT_VAT_CODE'])
        #expect a result
        self.assertGreater(len(result),0,'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'IT_VAT_CODE')
        #Check score
        self.assertGreaterEqual(result[0].score,0.5)
        
        # context enhancement
        # add context word
        test_str = 'piva ' + test_str
        result = analyze_text(test_str,['IT_VAT_CODE'])

        #expect a result
        self.assertGreater(len(result),0,'Result is empty')

        #check correct entity type
        self.assertEqual(result[0].entity_type, 'IT_VAT_CODE')

        #check the score, making sure it increases from the previous test
        self.assertGreaterEqual(result[0].score,1.0)


        # negative test case
        #invalid vat number
        test_str = '00000000000'
        result = analyze_text(test_str,['IT_VAT_CODE'])

        # expect an empty list
        self.assertEqual(len(result),0)


if __name__ == '__main__':
    unittest.main()
