import unittest
import random
from MergeSort import mergeSort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.data_1 = [x for x in range(1, 11)]
        random.shuffle(self.data_1)

    def test_MergeSort(self):
        sorted_data_1 = mergeSort(self.data_1)

        self.assertEqual(sorted_data_1[0], 1)
        self.assertEqual(sorted_data_1[1], 2)
        self.assertEqual(sorted_data_1[2], 3)
        self.assertEqual(sorted_data_1[3], 4)
        self.assertEqual(sorted_data_1[4], 5)
        self.assertEqual(sorted_data_1[5], 6)
        self.assertEqual(sorted_data_1[6], 7)
        self.assertEqual(sorted_data_1[7], 8)
        self.assertEqual(sorted_data_1[8], 9)
        self.assertEqual(sorted_data_1[9], 10)

if __name__ == '__main__':
    unittest.main()
