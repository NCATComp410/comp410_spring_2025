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
        # positive test case
        prefix = "51"
        middle = "824 753"
        suffix = "556"

        test_string = prefix + " " + middle + " "+ suffix
        result = analyze_text(test_string, ["AU_ABN"])

        # expect a result
        self.assertGreater(len(result), 0, "Result is empty")

        # check correct enetity_type
        self.assertEqual(result[0].entity_type, "AU_ABN")

        # check the score
        self.assertEqual(result[0].score, 1.0)


        # context enhancement
        # add context work
        test_string = "abn " + test_string
        result = analyze_text(test_string, ["AU_ABN"])

        # expect a result
        self.assertGreaterEqual(len(result), 0, "Result is empty")

        # check correct enetity_type
        self.assertEqual(result[0].entity_type, "AU_ABN")

        # check the score
        self.assertEqual(result[0].score, 1.0)



        # negative test case
        # Too long and wrong amount of leading numbers
        test_string = "000 00 000 000"
        result = analyze_text(test_string, ["AU_ABN"])

        # expect an empty list
        self.assertEqual(len(result), 0)


    def test_au_acn(self):
        """Test AU_ACN functionality"""

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
