"""Unit test file for team code_crafters"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_code_crafters(unittest.TestCase):
    """Test team code_crafters PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_in_aadhaar(self):
        """Test IN_AADHAAR functionality"""

    def test_in_pan(self):
        """Test IN_PAN functionality"""

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""
        #Positive test caase
        prefix = 'KL'
        second = '13'
        third = 'DL'
        last = '1999'
        test_string = prefix + '-'+second+'-'+third+'-'+last
        result = analyze_text(test_string, ['IN_VEHICLE_REGISTRATION'])
        #expect a result
        self.assertEqual(result, [])


        #check thre score
        

        #negative test case
        test_string = 'K-14-DL-03'
        result = analyze_text(test_string, ['IN_VEHICLE_REGISTRATION'])
        self.assertEqual(len(result), 0)
        


    def test_in_voter(self):
        """Test IN_VOTER functionality"""
    # positive Test Case
        letter_one = "A"
        letter_two = "B"
        letter_three = "C"
        numbers = "1234567"
        pos_test_one = ''.join((letter_one, letter_two, letter_three, numbers))
        result = analyze_text(pos_test_one, ['IN_VOTER'])
        self.assertEqual(result[0].entity_type, 'IN_VOTER')
        self.assertGreater(len(result), 0, "Result is empty")
        self.assertEqual(result[0].score, .4)
        
        # negative Test Case
        # too short
        neg_test_one = "ABC123456"
        result = analyze_text(neg_test_one, ['IN_VOTER'])
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
