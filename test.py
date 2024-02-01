#! /usr/bin/python3
import unittest
from Prog1 import sum

class TestSum(unittest.TestCase):
  def test_list_int(self):
    data = [10,9]
    result = sum(data)
    self.assertEqual(resutl,55)

if __name__ = '__main__':
  unittest.main()
