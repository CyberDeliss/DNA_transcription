import unittest
from utilities import plot_gc_ratio
from unittest.mock import patch


WRONG_MESSAGE = ""
EMPTY_MESSAGE = ""


class TestPlotGC(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_basic(self):
        dna_string = "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
        step = 10
        expected = None

        with patch('utilities.create_img') as mocked_create_img:
            mocked_create_img.return_value = True
            actual = plot_gc_ratio(dna_string, step)

        self.assertIsNone(actual, f"{actual}. But should be {expected}")

    def test_no_str(self):
        pass

    def test_step_is_int(self):
        pass

    def test_step_lower_0(self):
        pass

    def test_img_create(self):
        pass

    def test_step_is_float(self):
        pass


if __name__ == '__main__':
    unittest.main()
