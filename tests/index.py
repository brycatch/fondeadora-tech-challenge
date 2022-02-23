import unittest
from src.index import get_flat_array, item_is_array, validate_type_element
from constants import BIG_INPUT, BIG_OUTPUT


class TestIndex(unittest.TestCase):
    def test_item_is_array_array(self):
        item = []
        self.assertEqual(item_is_array(item), True)

    def test_item_is_array_number(self):
        item = 1
        self.assertEqual(item_is_array(item), False)

    def test_item_is_array_text(self):
        item = "1"
        self.assertEqual(item_is_array(item), False)

    def test_validate_type_element_text(self):
        item = "1"
        self.assertRaises(TypeError, validate_type_element, item)

    def test_validate_type_element_float(self):
        item = 1.2
        self.assertRaises(TypeError, validate_type_element, item)

    def test_case_1(self):
        inputs = [1, [2, [3, [[4, 5], 1, 6], 2], 6]]
        output = [1, 2, 3, 4, 5, 1, 6, 2, 6]
        self.assertEqual(get_flat_array(inputs), output)

    def test_case_2(self):
        inputs = [1, [2, [3, [4, 5]]]]
        output = [1, 2, 3, 4, 5]
        self.assertEqual(get_flat_array(inputs), output)

    def test_case_3(self):
        inputs = [1, 2, [1, 2, [14, 1, 3]], 3, [1, [2, 3], 4, [2, 3, 4]]]
        output = [1, 2, 1, 2, 14, 1, 3, 3, 1, 2, 3, 4, 2, 3, 4]
        self.assertEqual(get_flat_array(inputs), output)

    def test_case_4(self):
        inputs = [1, [2, [3, [4, 5, [1, 3, [4, 5, [9, [1, [[[[10]]]]]]]]]]]]
        output = [1, 2, 3, 4, 5, 1, 3, 4, 5, 9, 1, 10]
        self.assertEqual(get_flat_array(inputs), output)

    def test_case_5(self):
        inputs = [1, 1, 4, [1, [123], [2, [3, [4, 5]]]]]
        output = [1, 1, 4, 1, 123, 2, 3, 4, 5]
        self.assertEqual(get_flat_array(inputs), output)

    def test_case_6(self):
        inputs = [1, 2, 3, [1, 2, 3, 4, [2, 3, 4]]]
        output = [1, 2, 3, 1, 2, 3, 4, 2, 3, 4]
        self.assertEqual(get_flat_array(inputs), output)

    def test_case_7(self):
        inputs = BIG_INPUT
        output = BIG_OUTPUT
        self.assertEqual(get_flat_array(inputs), output)


if __name__ == "__main__":
    unittest.main()
