"""Unit test file for team tech_titans"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_tech_titans(unittest.TestCase):
    """Test team tech_titans PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

        # TODO: positive test case
        pref = '902'
        mid = '63'
        suff = '3013'
        test_str = '-'.join([pref, mid, suff])
        result = analyze_text(test_str, ["US_ITIN"])

            # first, expect a result
        self.assertGreater(len(result), 0, "Result is empty--likely from mismatch")

            # check correct entity type
        self.assertEqual(result[0].entity_type, "US_ITIN")

        # TODO: negative test case
            # US ITINs MUST begin with a '9'
        pref = '802'
        mid = '63'
        suff = '3013'
        test_str = '-'.join([pref, mid, suff])
        result = analyze_text(test_str, ["US_ITIN"])

            # expect an empty list (match not found)
        self.assertEqual(len(result), 0)

        # TODO: context enhancements


    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
