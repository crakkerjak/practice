#!/usr/bin/python3
import unittest
import practice

class TestPractice(unittest.TestCase):
    def test_min_range_in_k_sorted_lists(self):
        lists = [[4, 10, 15, 24, 26],
                [0, 9, 12, 20],
                [5, 18, 22, 30]]
        self.assertEqual(practice.min_range_in_k_sorted_lists(lists), (20, 24))

    def test_max_diff_subarrays_1(self):
        A = [-1, 1]
        expected = [(2, (0, 0), (1, 1)), (2, (1, 1), (0, 0))]
        self.assertIn(practice.max_diff_subarrays(A), expected)

    def test_max_diff_subarrays_2(self):
        A = [-1, 1, 1, 1, -1, -1]
        expected = [(5, (1, 3), (4, 5)), (5, (4, 5), (1, 3))]
        self.assertIn(practice.max_diff_subarrays(A), expected)

    def test_max_diff_subarrays_3(self):
        A = [4, -1, 7]
        expected = [(8, (1, 1), (2, 2)), (8, (2, 2), (1, 1))]
        self.assertIn(practice.max_diff_subarrays(A), expected)

    def test_longest_palindrome_1(self):
        s = 'aha'
        expected = 'aha'
        self.assertEqual(practice.longest_palindrome(s), expected)

    def test_longest_palindrome_2(self):
        s = 'ttaatta'
        expected = ['attatta', 'ttaaatt', 'tatatat']
        self.assertIn(practice.longest_palindrome(s), expected)

    def test_longest_palindrome_3(self):
        s = 'abc'
        expected = ['a', 'b', 'c']
        self.assertIn(practice.longest_palindrome(s), expected)

    def test_longest_palindrome_4(self):
        s = 'gggaaa'
        expected = ['agaga', 'gagag', 'aggga', 'gaaag']
        self.assertIn(practice.longest_palindrome(s), expected)

    def test_probability_of_alive_1(self):
        self.assertEqual(practice.probability_of_alive(3,1,1,0), 1)

    def test_probability_of_alive_2(self):
        self.assertEqual(practice.probability_of_alive(3,1,1,1), 1)

    def test_probability_of_alive_3(self):
        self.assertEqual(practice.probability_of_alive(3,1,1,2), 0.75)

    def test_probability_of_alive_4(self):
        self.assertEqual(practice.probability_of_alive(3,1,1,3), 0.375)

    def test_probability_of_alive_5(self):
        self.assertEqual(practice.probability_of_alive(5,0,0,1), 0.5)

    def test_probability_of_alive_6(self):
        self.assertEqual(practice.probability_of_alive(2,0,0,2), 0.125)

if __name__ == '__main__':
    unittest.main()
