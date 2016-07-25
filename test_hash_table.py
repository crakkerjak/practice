#!/usr/bin/python3

import unittest
import hash_table

class TestHashTable(unittest.TestCase):

    def test_hast_table_1(self):
        ht = hash_table.hash_table()
        ht.put(1, 's')

        actual = ht.get(1)
        expected = 's'
        self.assertEqual(actual, expected)

    def test_hast_table_2(self):
        ht = hash_table.hash_table()
        ht.put(1, 's')

        actual = ht.get(10)
        expected = None
        self.assertEqual(actual, expected)

    def test_hast_table_3(self):
        ht = hash_table.hash_table()

        actual = ht.get(1)
        expected = None
        self.assertEqual(actual, expected)

    def test_hast_table_4(self):
        ht = hash_table.hash_table()
        ht.put(1, 's')
        ht.put(10, 's' * 10)

        actual = ht.get(1)
        expected = 's'
        self.assertEqual(actual, expected)

        actual = ht.get(10)
        expected = 's' * 10
        self.assertEqual(actual, expected)

    def test_hast_table_5(self):
        ht = hash_table.hash_table()
        for i in range(1000):
            ht.put('a' * i, i / 2)

        for i in range(1000):
            actual = ht.get('a' * i)
            expected = i / 2
            self.assertEqual(actual, expected)

    def test_hast_table_6(self):
        ht = hash_table.hash_table()
        ht.put(1, 's')

        actual = ht.get(1)
        expected = 's'
        self.assertEqual(actual, expected)

        ht.put(1, 't')
        actual = ht.get(1)
        expected = 't'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
