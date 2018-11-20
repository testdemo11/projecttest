#-*-coding: UTF-8-*-
#Author: Tnew

import sys
sys.path.append("D:\OneDrive\Study\Python\pythonstudy\projects")
from forunittest.calculator import Count
import unittest

class TestAdd(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(21,42)
        self.assertEqual(j.add(),63)

if __name__ == '__main__':
    unittest.main()