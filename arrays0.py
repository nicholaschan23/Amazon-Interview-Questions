"""
https://www.codinginterview.com/amazon-interview-questions
Problem statement:
You are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
"""
def findMissingNum(dist_nums: list, n: int):
    # precondition: list distinct numbers from 0 to n
    # https://www.wikihow.com/Sum-the-Integers-from-1-to-N
    return (n*(n + 1)/2) - sum(dist_nums, 0)

import unittest
class Testing(unittest.TestCase):
    def test0(self):
        a = [0, 1, 2, 3, 4, 5, 6, 8]
        n = 8
        self.assertEqual(findMissingNum(a, n), 7)
    def test1(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        n = 8
        self.assertEqual(findMissingNum(a, n), 0)
    def test2(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        n = 8
        self.assertEqual(findMissingNum(a, n), 8)
    def test3(self):
        a = []
        n = 0
        self.assertEqual(findMissingNum(a, n), 0)

if __name__ == '__main__':
    unittest.main()