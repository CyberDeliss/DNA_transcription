import unittest
from utilities import plot_gc_ratio
from unittest.mock import patch


WRONG_MESSAGE = "Your DNA string is wrong"
EMPTY_MESSAGE = ""


class TestPlotGC(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_basic(self):
        dna_string = "ATTTGGCTACTAACAATCTA"
        expected = True

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string)

        self.assertTrue(actual, f"{actual}. But should be {expected}")

    def test_dna_no_str(self):
        dna_string = 123
        step = 10
        expected = False
        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")

    def test_step_isnt_int(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        step = 10.12345
        expected = False

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")

    def test_step_lower_0(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        step = -1
        expected = False

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")

    def test_step_lower_0_and_is_float(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        step = -1.345
        expected = False

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")

    def test_img_create(self):
        # TODO add os
        pass

    def test_step_is_string(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        step = "10"
        expected = False

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")

    def test_dna_lower(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT".lower()
        step = 10
        expected = True

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")

    def test_dna_wrong_alphabet(self):
        dna_string = "sdfg5678_=865 5+* # <<>/.\|| <> hhn".lower()
        step = 10
        expected = False

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertFalse(actual, f"{actual}. But should be {expected}")


if __name__ == '__main__':
    unittest.main()
