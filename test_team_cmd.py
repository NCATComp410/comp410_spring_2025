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
        #positve test case
        nums = "12345678"
        let = "Z"
        test_str = "-".join([nums, let])
        result = analyze_text(test_str, ['ES_NIF'])
        #expect a result
        self.assertGreater(len(result), 0, "result is")
        #check correct entity type
        self.assertEqual(result[0].entity_type, 'ES_NIF')

        #negative test case

        #context enhancement

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
