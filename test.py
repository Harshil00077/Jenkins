#! /usr/bin/python3
import unittest
from Prog1 import sum

class TestSum(unittest.TestCase):
  def test_list_int(self):
    a = 10
    b = 20
    data = [a,b]
    result = sum(data)
    self.assertEqual(resutl,a+b)

if __name__ = '__main__':
  unittest.main()
