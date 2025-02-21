"""Unit test file for team tech_titans"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_tech_titans(unittest.TestCase):
    """Test team tech_titans PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_URL(self):
        """Test URL functionality"""
         # Positive test case: Basic URL
        test_str = "www.tamu.edu"
        result = analyze_text(test_str, ['URL'])
        #expect a result
        print(result)
        # Making sure that a result is returned
        self.assertGreater(len(result), 0, "Expected at least one entity to be detected.")
        #  detected entity is a URL
        self.assertEqual(result[0].entity_type, 'URL', "Entity type should be 'URL'.")
        # Score check
        self.assertEqual(result[0].score, 0.5)

        # context enhancement with a context word
        test_url_string = 'link ' + 'www.tamu.edu'
        result = analyze_text(test_url_string, ['URL'])
        # Making sure that a result is returned
        print(result)
        self.assertGreater(len(result), 0, "Expected at least one entity to be detected.")
        # detected entity is a URL
        self.assertEqual(result[0].entity_type, 'URL', "Entity type should be 'URL'.")
        # Score check
        self.assertEqual(result[0].score, 0.85)

        # Negative test case: No URL present
        test_str_no_url = "This text does not contain any URLs."
        result_no_url = analyze_text(test_str_no_url, ['URL'])
        print(result_no_url)
        # Assert no entities are detected
        self.assertEqual(len(result_no_url), 0, "Expected no entities to be detected.")


    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""
        #positive test case
        #Valid bank number
        test_bank_str = '19433758376'
        result = analyze_text(test_bank_str, ['US_BANK_NUMBER'])
        #expect a result
        print(result)
        self.assertGreater(len(result), 0, 'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'US_BANK_NUMBER')
        #Check score
        self.assertEqual(result[0].score, 0.05)

        # context enahancement with context word
        test_bank_str = 'check ' + '19433758376'
        result = analyze_text(test_bank_str, ['US_BANK_NUMBER'])
        #expect a result
        print(result)
        self.assertGreater(len(result), 0, 'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'US_BANK_NUMBER')
        #Check score
        self.assertEqual(result[0].score, 0.40)



        # negative test case
        # Too short to be a bank number
        test_bank_str = '123485'
        result = analyze_text(test_bank_str, ['US_BANK_NUMBER'])
        #expect an empty list
        self.assertEqual(len(result), 0)


        #context enhancement


    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

        # positive test case
        # making an example string
        test_str = "12345678"
        result = analyze_text(test_str, ['US_DRIVER_LICENSE'])
        #expect result
        self.assertGreater(len(result), 0, 'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'US_DRIVER_LICENSE')
        #check score
        self.assertEqual(result[0].score, .01)

        #context enhance
        #adding context word
        test_str = 'license ' + test_str
        result = analyze_text(test_str, ['US_DRIVER_LICENSE'])
        #expect result
        self.assertGreater(len(result), 0, 'Result is empty')
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'US_DRIVER_LICENSE')
        #check score
        self.assertEqual(result[0].score, 0.4)
        
        # negative test case
        # too short
        test_str = "1234"
        result = analyze_text(test_str, ['US_DRIVER_LICENSE'])
        # expect empty list
        self.assertEqual(len(result), 0)


    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
