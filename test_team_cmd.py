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

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""
        pos_test_cases = [
                            "DE44500105175407324931", 
                            "FR7630006000011234567890189",  
                            "ES9121000418450200051332", 
                            "IT60X0542811101000000123456"
                        ]
        neg_test_cases = [
                        "DE4450010517540732",  # Too short
                        "FR7630006000011234567890189123",  # Too long
                        "IT60X0542811101O00000123456",  # Non-numeric character (O instead of 0)
                        "NL91ABNA!417164300",  # Special character included (!)
                        "GB29 NW BK60161331926819",  # Extra spaces
                        "SA0280000000608010167519",  # Incorrect check digits
                        "AE070331234567890123546"  # Swapped digits
                    ]

        #without context tests
        for x in pos_test_cases:
            results = analyze_text(f"{x}",["IBAN_CODE"])

            self.assertGreater(len(results),0) #asserting a full list for a detected code

            self.assertGreaterEqual(results[0].score, 0.5) #valid IBAN
            self.assertEqual(results[0].entity_type, 'IBAN_CODE') #validating entity type

        for x in neg_test_cases:
            results = analyze_text(f"{x}",["IBAN_CODE"])
            self.assertEqual(len(results),0) #asserting an empty list for an undetected code

        
        #with context tests
        for x in pos_test_cases:
            results = analyze_text(f"IBAN CODE: {x}",["IBAN_CODE"])

            self.assertGreater(len(results),0) #asserting a full list for a detected code

            self.assertGreaterEqual(results[0].score, 0.5) #valid IBAN
            self.assertEqual(results[0].entity_type, 'IBAN_CODE') #validating entity type

        for x in neg_test_cases:
            results = analyze_text(f"IBAN CODE: {x}",["IBAN_CODE"])
            self.assertEqual(len(results),0) #asserting an empty list for an undetected code

        

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
