import unittest
from translator import english_to_french, french_to_english


class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Salut"), "Dog")


class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Dog"), "Salut")


if __name__ == '__main__':
    unittest.main()
    print("No errors")
