import unittest
from unittest.mock import patch
from data.base_classes import convert_dna_to_rna
from data.create_db import connect_dna_and_rna

WRONG_MESSAGE = "Your DNA string is wrong"
EMPTY_MESSAGE = "Your DNA string is empty"


class TestConvertDNAtoRNA(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ""
        self.dna_bases, self.rna_bases = connect_dna_and_rna()

    def get_rna_list(self, dna_string: str) -> list:
        rna_objects = []
        for letter in dna_string:
            for base in self.dna_bases:
                if letter == str(base.name):
                    rna_objects.append(base.rna)
                    break
        return rna_objects

    def test_basic(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        expected = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"

        rna_list = self.get_rna_list(dna_string)
        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [rna for rna in rna_list]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_dna_has_numeric_symbols(self):
        dna_string = "123456789"
        expected = WRONG_MESSAGE
        actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"Should be {expected}")

    def test_contains_invalid_letters(self):
        dna_string = "cvgbhjnkpARTREDopoiuy6789/.*64n cvbj"
        expected = WRONG_MESSAGE
        actual = convert_dna_to_rna(self.db, dna_string)

        self.assertTrue(actual == expected, f"Should be {expected}")

    def test_a_lot_of_letters(self):
        dna_string = ""
        for _ in range(0, 100000):
            dna_string += "ACTG"

        expected = ""
        for _ in range(0, 100000):
            expected += "ACUG"

        rna_list = self.get_rna_list(dna_string)

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [rna for rna in rna_list]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_empty_string(self):
        dna_string = ""
        expected = EMPTY_MESSAGE

        rna_list = self.get_rna_list(dna_string)

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [rna for rna in rna_list]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_att(self):
        dna_string = "ATT"
        expected = "AUU"

        rna_list = self.get_rna_list(dna_string)

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [rna for rna in rna_list]
            actual = convert_dna_to_rna(self.db, dna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")


if __name__ == '__main__':
    unittest.main()
