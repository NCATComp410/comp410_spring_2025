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

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

        # Positive Test Case 
        test_str = "My medicare is: 5088193576"
        result = analyze_text(test_str, ['AU_MEDICARE']) # Analyze_Text will find the Medicare & store associated information
        self.assertGreater(len(result), 0) # Result should contain atleast one identified medicare number


        # Negative Test Case 
        test_str = "980-122-3241"
        result = analyze_text(test_str, ['AU_MEDICARE'])
        self.assertEqual(len(result), 0) # Invalid test string should result in an empty list 



    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
