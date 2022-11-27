import unittest
from unittest.mock import patch, Mock
from data.base_classes import convert_dna_to_rna

DNA_LETTER_CONVERT = {
    "A": "A",
    "C": "C",
    "G": "G",
    "T": "U"
}
WRONG_MESSAGE = "Your DNA string is wrong"

# mock = Mock()
# mock.method.return_value = [3, 2]
# print(mock.method())


class TestConvertDNAtoRNA(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ""

    def test_basic(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        expected = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"

        with patch('data.base_classes.convert_dna_letter_to_rna_letter') as mocked_rna_letter:
            mocked_rna_letter.side_effect = [DNA_LETTER_CONVERT[dna] for dna in dna_string]
            actual = convert_dna_to_rna(self.db, dna_string)

        print([DNA_LETTER_CONVERT[dna] for dna in dna_string])
        self.assertTrue(actual == expected, f"{actual}. But should be {expected}")

    def test_dna_no_str(self):
        dna_string = "123456789"
        expexted = WRONG_MESSAGE
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_dna_lower(self):
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_dna_register_is_various(self):
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_contains_invalid_letters(self):
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_a_lot_of_letters(self):
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_too_few_letters(self):
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")


if __name__ == '__main__':
    unittest.main()
