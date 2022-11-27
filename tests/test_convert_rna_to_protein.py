import unittest
from unittest.mock import patch
from data.base_classes import convert_rna_to_protein
from data.genetic_codes import GENETIC_CODE_REVERSE, AMINO_FULL_NAME
from data.base_classes import AminoAcids

WRONG_MESSAGE = "Your RNA string is wrong"
EMPTY_MESSAGE = "Your RNA string is empty"


class TestConvertDNAtoRNA(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ""

    def test_basic(self):
        rna_string = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
        codons = [rna_string[i:i + 3] for i in range(0, len(rna_string), 3)]
        expected = "PVLDWLEEKF"

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

        with patch('data.base_classes.convert_codon_to_amino') as mocked_amino:
            mocked_amino.side_effect = aminos
            actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_rna_has_numeric_symbols(self):
        rna_string = "CCC12GUCCUUGAUUGG0CUUGAAGAGAAGUUU"
        expected = WRONG_MESSAGE

        actual = convert_rna_to_protein(self.db, rna_string)
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_rna_lower(self):
        pass

    def test_dna_register_is_various(self):
        pass

    def test_contains_invalid_letters(self):
        pass

    def test_a_lot_of_letters(self):
        pass

    def test_empty_string(self):
        pass


if __name__ == '__main__':
    unittest.main()
