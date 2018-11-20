#-*-coding: UTF-8-*-
#Author: Tnew

import sys
sys.path.append("D:\OneDrive\Study\Python\pythonstudy\projects")
from forunittest.calculator import Count
import unittest

class TestSub(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_sub(self):
        j = Count(5,3)
        self.assertEqual(j.sub(),2)

    def test_sub2(self):
        j = Count(21,42)
        self.assertEqual(j.sub(),-21)

if __name__ == '__main__':
    unittest.main()