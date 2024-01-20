import unittest
from src.maximum_average_subarray_i import maximum_average_subarray_i


class TestMaximumaveragesubarrayi(unittest.TestCase):
    def test_maximum_average_subarray_i_1(self):
        """
        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
        """
        self.assertEqual(
            maximum_average_subarray_i(nums=[1, 12, -5, -6, 50, 3], k=4), 12.75000
        )

    def test_maximum_average_subarray_i_2(self):
        """
        Input: nums = [5], k = 1
        Output: 5.00000
        """
        self.assertEqual(maximum_average_subarray_i(nums=[5], k=1), 5.00000)


if __name__ == "__main__":
    unittest.main()
