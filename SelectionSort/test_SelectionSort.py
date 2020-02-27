import unittest
import random
from SelectionSort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.data_1 = [x for x in range(1, 11)]
        random.shuffle(self.data_1)

    def test_SelectionSort(self):
        selection_sort(self.data_1)

        self.assertEqual(self.data_1[0], 1)
        self.assertEqual(self.data_1[1], 2)
        self.assertEqual(self.data_1[2], 3)
        self.assertEqual(self.data_1[3], 4)
        self.assertEqual(self.data_1[4], 5)
        self.assertEqual(self.data_1[5], 6)
        self.assertEqual(self.data_1[6], 7)
        self.assertEqual(self.data_1[7], 8)
        self.assertEqual(self.data_1[8], 9)
        self.assertEqual(self.data_1[9], 10)

if __name__ == '__main__':
    unittest.main()
