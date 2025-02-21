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

    def setUp(self):
        """Initialize the Presidio Analyzer Engine with AU_TFN Recognizer."""
        self.analyzer = AnalyzerEngine()

        # Define a pattern for AU TFN (9 digits, with or without spaces/hyphens)
        tfn_pattern = Pattern(name="AU_TFN", regex=r"\b\d{3}[- ]?\d{3}[- ]?\d{3}\b", score=0.8)

        # Register a custom recognizer for AU_TFN
        self.au_tfn_recognizer = PatternRecognizer(supported_entity="AU_TFN", patterns=[tfn_pattern])
        self.analyzer.registry.add_recognizer(self.au_tfn_recognizer)

    def test_au_tfn(self):
        #positive test case
        """Test AU_TFN detection (Positive Test Case)"""
        test_cases = [
            "My tax file number is 123-456-789",
            "Here is my TFN: 123 456 789",
            "TFN: 123456789 should be detected.",
            "AU TFN: 987-654-321 is a valid identifier."
        ]

        for text in test_cases:
            with self.subTest(text=text):
                results = self.analyzer.analyze(text=text, entities=["AU_TFN"], language="en")
                
                # Print result for debugging
                print(f"Test case: {text} → Results: {results}")

                # Ensure at least one result is found
                self.assertGreater(len(results), 0, f"AU_TFN was not detected in: {text}")

                # Check the correct entity type
                self.assertEqual(results[0].entity_type, "AU_TFN", f"Incorrect entity detected in: {text}")

              # negative case
        #too short
        test_str = '123456789'
        result = analyze_text(test_str, ['AU_TFN'])
        #expect a empty list
        self.assertEqual(len(result), 0)  

if __name__ == '__main__':
    unittest.main()
