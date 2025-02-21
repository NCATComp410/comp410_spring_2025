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
        # Example FI PIDs:
        #     VALID: 131052-308T
        #     041404A123X
        #     VALID: 150395-123K
        # positive test case
        date = "131052"
        separator_char = '-'
        indiv_num = '308T'
        control_char = 'T'
        test_str = date + separator_char+ indiv_num + control_char
        results = analyze_text(test_str,['FI_PERSONAL_IDENTITY_CODE'])
        #expect a result
        self.assertGreater(len(results),0,'Result is Empty :(')
        #check correct entity type
        self.assertEqual(results[0].entity_type,'FI_PERSONAL_IDENTITY_CODE')
       # Check the score
        self.assertEqual(results[0].score, 1)


       # context enhancement(adding a context word)
        """ 
        None of  the context words(CW) actually improve the score. W/o any of the CWs the test string preforms fine(score =1.0). 
        With the CWs however, the original score drops to 0.1 and the CW INCREASES the score to .9. Bringing it back to 1.0...
        """

        context_words = ["hetu", "henkilötunnus", "personbeteckningen", "personal identity code"]
        test_str = context_words[0] +  test_str
        results = analyze_text(test_str,['FI_PERSONAL_IDENTITY_CODE'])
        #expect a result
        self.assertGreater(len(results),0,'Result is Empty :(')
        #check correct entity type
        self.assertEqual(results[0].entity_type,'FI_PERSONAL_IDENTITY_CODE')
       # Check the score
        self.assertEqual(results[0].score, 1)

       # negative test case
        test_str = "041404A123X"
        results = analyze_text(test_str,['FI_PERSONAL_IDENTITY_CODE'])
        self.assertEqual(len(results),0)

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
