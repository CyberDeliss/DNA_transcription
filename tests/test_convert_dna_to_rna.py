import unittest
from unittest.mock import patch
from data.base_classes import convert_dna_to_rna
from data.base_classes import DnaBase, RnaBase

WRONG_MESSAGE = "Your DNA string is wrong"
EMPTY_MESSAGE = "Your DNA string is empty"


class TestConvertDNAtoRNA(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ""
        self.temp = connect_rna_and_dna()
        self.dna_bases = self.temp[0]
        self.rna_bases = self.temp[1]

    def test_basic(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        expected = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"

        rna_list = get_rna_list(dna_string, self.dna_bases)

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [rna for rna in rna_list]
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


def create_dna_list() -> list:
    dna_bases = []
    temp_id = 0
    for letter in "ACGT":
        temp_id += 1
        dna_bases.append(DnaBase(id=temp_id, name=letter))
    return dna_bases


def create_rna_list() -> list:
    temp_id = 0
    rna_bases = []
    for letter in "ACGU":
        temp_id += 1
        rna_bases.append(RnaBase(id=temp_id, name=letter))
    return rna_bases


def connect_rna_and_dna() -> list:
    dna_bases = create_dna_list()
    rna_bases = create_rna_list()

    for dna in dna_bases:
        for rna in rna_bases:
            if str(dna.name) == str(rna.name):
                dna.rna = rna
                dna.rna_id = rna.id
                break
            elif str(dna.name) == "T":
                if str(rna.name) == "U":
                    dna.rna = rna
                    dna.rna_id = rna.id
                    break
    return [dna_bases, rna_bases]


def get_rna_list(dna_string: str, dna_bases: list) -> list:
    rna_objects = []
    for letter in dna_string:
        for base in dna_bases:
            if letter == str(base.name):
                rna_objects.append(base.rna)
    return rna_objects


if __name__ == '__main__':
    unittest.main()
