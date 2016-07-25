#!/usr/bin/python3
import unittest
import hash_table

class TestHashTable(unittest.TestCase):
    '''Unit test class for basic hash table functionality.

    Tests get, put, and remove methods in a hash_table class.
    '''

    def test_hash_table_1(self):
        '''Puts one k, v pait and checks to see that get returns v'''
        ht = hash_table.HashTable()
        ht.put(1, 's')

        actual = ht.get(1)
        expected = 's'
        self.assertEqual(actual, expected)

    def test_hash_table_2(self):
        '''Puts then gets a different key.'''
        ht = hash_table.HashTable()
        ht.put(1, 's')

        actual = ht.get(10)
        expected = None
        self.assertEqual(actual, expected)

    def test_hash_table_3(self):
        '''Gets from an empty table.'''
        ht = hash_table.HashTable()

        actual = ht.get(1)
        expected = None
        self.assertEqual(actual, expected)

    def test_hash_table_4(self):
        '''Puts and gets 2 distinct k, v pairs.'''
        ht = hash_table.HashTable()
        ht.put(1, 's')
        ht.put(10, 's' * 10)

        actual = ht.get(1)
        expected = 's'
        self.assertEqual(actual, expected)

        actual = ht.get(10)
        expected = 's' * 10
        self.assertEqual(actual, expected)

    def test_hash_table_5(self):
        '''Puts and gets 1000 distinct k, v pairs.'''
        ht = hash_table.HashTable()
        for i in range(1000):
            ht.put('a' * i, i / 2)

        for i in range(1000):
            actual = ht.get('a' * i)
            expected = i / 2
            self.assertEqual(actual, expected)

    def test_hash_table_6(self):
        '''Puts verifies value, updates, verfies new value. Same key.'''
        ht = hash_table.HashTable()
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
