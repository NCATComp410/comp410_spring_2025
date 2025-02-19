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
        # positive test case *returning empty list
        prefix = 'X'
        middle = '1234567'
        suffix = 'A'
        test_str = prefix + middle + suffix
        result = analyze_text(test_str, ['ES_NIE'])
        # expect value in result list
        self.assertGreater(len(result),0, 'Result is empty')
        # checking entity type is actually first elements
        self.assertEqual(result[0].entity_type, 'ES_NIE')
        # check the score ?
        self.assertEqual(result[0].score, 0.5)

        # context enhancement
        # add context word
        test_str = 'NIE' + test_str
        result = analyze_text(test_str, ['ES_NIE'])
        # expect value in result list
        self.assertGreater(len(result),0, 'Result is empty')
        # checking entity type is actually first elements
        self.assertEqual(result[0].entity_type, 'ES_NIE')
        # check the score ?
        self.assertEqual(result[0].score, 0.85)

        # negative test case
        # first letter is not X,Y, or Z
        test_str = 'A1234567Z'
        result = analyze_text(test_str, ['ES_NIE'])
        # expect empty list
        self.assertEqual(len(result), 0)

    def test_es_nif(self):
        """Test ES_NIF functionality"""

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
