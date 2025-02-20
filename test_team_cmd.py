"""Unit test file for team cmd"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_cmd(unittest.TestCase):
    """Test team cmd PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_es_nie(self):
        """Test ES_NIE functionality"""

    def test_es_nif(self):
        """Test ES_NIF functionality"""
        #positve test cases
        nums = "12345678"
        let = "Z"
        base_str = "-".join([nums, let])
        context_list = [""," documento nacional de identidad ", " DNI ", " NIF ", " identificación "]

        for context in context_list:
            test_str = base_str + context
            result = analyze_text(test_str,["ES_NIF"])
            self.assertGreater(len(result), 0, "result is")
            self.assertEqual(result[0].entity_type, 'ES_NIF')

        for context in context_list:
            test_str = context + base_str
            result = analyze_text(test_str,["ES_NIF"])
            self.assertGreater(len(result), 0, "result is")
            self.assertEqual(result[0].entity_type, 'ES_NIF')
            
        #negative test case
        #invalid_nif = [too short, too long, too many letters, no letters, invaild checksum]
        invalid_nif = ["345274-A","3452723224-A","3457274-AB","12345678","12345677-Z"]

        for test_str in invalid_nif:
            result = analyze_text(test_str,["ES_NIF"])
            self.assertEqual(len(result), 0)

        

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
