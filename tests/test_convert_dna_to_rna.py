import unittest
from unittest.mock import patch
from data.base_classes import convert_dna_to_rna

DNA_LETTER_CONVERT = {
    "A": "A",
    "C": "C",
    "G": "G",
    "T": "U"
}

WRONG_MESSAGE = "Your DNA string is wrong"
EMPTY_MESSAGE = "Your DNA string is empty"


class TestConvertDNAtoRNA(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ""

    def test_basic(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        expected = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [DNA_LETTER_CONVERT[dna] for dna in dna_string]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_dna_has_numeric_symbols(self):
        dna_string = "123456789"
        expected = WRONG_MESSAGE
        actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"Should be {expected}")

    def test_dna_lower(self):
        dna_string = "gctaactaacatctttggcactgtt"
        expected = "GCUAACUAACAUCUUUGGCACUGUU"

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [DNA_LETTER_CONVERT[dna.title()] for dna in dna_string]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_dna_register_is_various(self):
        dna_string = "gctaactaaCAtcTTtGgcactgtt"
        expected = "GCUAACUAACAUCUUUGGCACUGUU"

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [DNA_LETTER_CONVERT[dna.title()] for dna in dna_string]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_contains_invalid_letters(self):
        dna_string = "cvgbhjnkpARTREDopoiuy6789/.*64n cvbj"
        expected = WRONG_MESSAGE
        actual = convert_dna_to_rna(self.db, dna_string)

        self.assertTrue(actual == expected, f"Should be {expected}")

    def test_a_lot_of_letters(self):
        dna_string = ""
        for _ in range(0, 10000):
            dna_string += "ACTG"

        expected = ""
        for _ in range(0, 10000):
            expected += "ACUG"

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [DNA_LETTER_CONVERT[dna.title()] for dna in dna_string]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_empty_string(self):
        dna_string = ""
        expected = EMPTY_MESSAGE
        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [DNA_LETTER_CONVERT[dna.title()] for dna in dna_string]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")


if __name__ == '__main__':
    unittest.main()
