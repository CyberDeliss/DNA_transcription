import unittest
from data.base_classes import convert_dna_to_rna
from data.db import get_db


class TestConvertDNAtoRNA(unittest.TestCase):

    def setUp(self) -> None:
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_basic(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_dna_no_str(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_db_no_exist(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_dna_lower(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_letters_is_wrong(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_a_lot_of_letters(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")

    def test_too_few_letters(self):
        db = get_db()
        dna_string = ""
        expexted = ""
        actual = convert_dna_to_rna(db, dna_string)

        self.assertTrue(actual == expexted, f"Should be {expexted}")


if __name__ == '__main__':
    unittest.main()
