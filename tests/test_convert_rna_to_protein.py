import unittest
from unittest.mock import patch
from data.base_classes import convert_rna_to_protein, get_codons
from data.genetic_codes import GENETIC_CODE_REVERSE, AMINO_FULL_NAME
from data.base_classes import AminoAcids

WRONG_MESSAGE = "Your RNA string is wrong"
EMPTY_MESSAGE = "Your RNA string is empty"


class TestConvertDNAtoRNA(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ""

    def test_basic(self):
        rna_string = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
        expected = "PVLDWLEEKF"

        with patch('data.base_classes.convert_codon_to_amino') as mocked_amino:
            mocked_amino.side_effect = create_aminos(rna_string)
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_rna_has_numeric_symbols(self):
        rna_string = "CCC12GUCCUUGAUUGG0CUUGAAGAGAAGUUU"
        expected = WRONG_MESSAGE

        actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_rna_lower(self):
        rna_string = "cccguccuugauuggcuugaagagaaguuu"
        expected = "PVLDWLEEKF"

        with patch('data.base_classes.convert_codon_to_amino') as mocked_amino:
            mocked_amino.side_effect = create_aminos(rna_string)
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_dna_register_is_various(self):
        rna_string = "CccguccuugaUUgGcuugaagagaaguuU"
        expected = "PVLDWLEEKF"

        with patch('data.base_classes.convert_codon_to_amino') as mocked_amino:
            mocked_amino.side_effect = create_aminos(rna_string)
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_contains_invalid_letters(self):
        rna_string = "TTT"
        expected = WRONG_MESSAGE
        actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_only_invalid_letters(self):
        rna_string = "567)))99+-<></><\>"
        expected = WRONG_MESSAGE
        actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_a_lot_of_letters(self):
        rna_string = ""
        for _ in range(0, 100000):
            rna_string += "UUGCGAGGUCCG"

        expected = ""
        for _ in range(0, 100000):
            expected += "LRGP"

        with patch('data.base_classes.convert_codon_to_amino') as mocked_amino:
            mocked_amino.side_effect = create_aminos(rna_string)
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_empty_string(self):
        rna_string = ""
        expected = EMPTY_MESSAGE

        with patch('data.base_classes.convert_codon_to_amino') as mocked_amino:
            mocked_amino.side_effect = create_aminos(rna_string)
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_rna_contain_not_all_letter(self):
        rna_string = "AUU"
        expected = "I"

        with patch('data.base_classes.convert_codon_to_amino') as mocked_rna_letter:
            mocked_rna_letter.side_effect = create_aminos(rna_string)
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")


def create_aminos(rna_string: str) -> list:
    codons = get_codons(rna_string)

    temp_id = 0
    keys = [GENETIC_CODE_REVERSE[codon] for codon in codons]

    aminos = []
    for key in keys:
        temp_id += 1
        aminos.append(
            AminoAcids(
                id=temp_id,
                short_name=key.capitalize(),
                middle_name=AMINO_FULL_NAME.get(key)[0].capitalize(),
                full_name=AMINO_FULL_NAME.get(key)[1].title()
            )
        )
    return aminos


if __name__ == '__main__':
    unittest.main()
