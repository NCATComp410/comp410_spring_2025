"""Unit test file for team 410_developers"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_410_developers(unittest.TestCase):
    """Test team 410_developers PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number_success(self):
        """TESTING Successful Routing Number Functionality"""
        #positive test case
        valid_routing_numbers = {
           "Truist": "061000104",
           "Bank Of America": "026009593"
        }


        for bank_name, routing_number in valid_routing_numbers.items():
            result = analyze_text(routing_number, entity_list=["ABA_ROUTING_NUMBER"])
            self.assertTrue(result, "Analyzer did not detect routing number")
            self.assertEqual("ABA_ROUTING_NUMBER", result[0].entity_type)




    def test_aba_routing_number_failure(self):
        """TESTING Failing Routing Number Functionality"""
        #negative test case
        invalid_routing_numbers = {
           "Fraudist": "0600IT777",
           "Fake Of America": "020ZY0999"
        }

        for bank_name, routing_number in invalid_routing_numbers.items():
            result = analyze_text(routing_number, entity_list=["ABA_ROUTING_NUMBER"])
            print(result)
            self.assertFalse(result, "Analyzed an incorrrect routing number")       

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
