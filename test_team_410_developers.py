"""Unit test file for team 410_developers"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_410_developers(unittest.TestCase):
    """Test team 410_developers PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        #postive test case
        prefix = "001"
        middle = "799"
        suffix = "837"
        test_str = prefix + " " + middle + " " + suffix
        result = analyze_text(test_str,["AU_ACN"])
 # expect result
        self.assertGreater(len(result), 0, "Result is empty")
 # check correct entity_type
        self.assertEqual(result[0].entity_type, "AU_ACN")
        #check the score 
        self.assertEqual(result[0].score,1.0)

        # #context enhancement
        # #add context word
        # test_str = test_str + 'acn','australian company number'
        # result = analyze_text(test_str,['AU_ACN'])
        # #expect a result
        # self.assertGreater(len(result),0,'Result is empty')
        # #check correct enitity_type
        # self.assertEqual(result[0].entity_type,'AU_ACN')
        # #check the score 
        # self.assertEqual(result[0].score,1.0)

        # #negative test cases
        # test_str = ['123-456-789','123 456 7']#these each have an error   
        # result = analyze_text(test_str, ['AU_ACN'])

        # # #expect an empty list
        # self.assertEqual(len(result), 0)

        


    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
