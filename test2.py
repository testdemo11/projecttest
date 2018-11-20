#  -*- coding:utf8 -*-
# @Time  : 2018/10/25 - 20:45
# @Author: Naraku
# @File  : test2.py

import sys
sys.path.append("D:\OneDrive\Study\Python\pythonstudy\projects")
from forunittest.count import is_prime
import unittest

class Test(unittest.TestCase):
    def setUp(self):
       print("test start")

    def test_case(self):
        self.assertTrue(is_prime(7),msg="Is not a prime.")

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()