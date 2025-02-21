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
        prefix = "123"#dealing with one piece at a time
        middle = "456"
        suffix = "789"
        test_str = prefix +' '+middle+' '+suffix
        #the one with spaces should work but w/o should work too 
        # test_str = "000 000 000"#seperated by blank spaces
        result = analyze_text(test_str,['AU_ACN'])
        #expect a result
        self.assertGreater(len(result),0,'Result is empty')
        #check correct enitity_type
        self.assertEqual(result[0].entity_type,'AU_ACN')

        #negative test cases
        # negative_auacns = ['123-456-789','123 456 7']#these each have an error        # negative_auacns =[ "123 456 7","abcdefghi","111 111 111"]#each has an error of some sort
        # result = analyze_text(negative_auacns, ['AU_ACN'])
        # #expect an empty list
        # self.assertEqual(len(result), 0)

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
