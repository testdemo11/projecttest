#  -*- coding:utf8 -*-
# @Time  : 2018/10/28 - 15:43
# @Author: Naraku
# @File  : testfixtures.py


import unittest

def setUpModule():
    print("test module start >>>")

def tearDwonModule():
    print("test module end >>>")


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start --->>>")

    @classmethod
    def tearDownClass(cls):
        print("test class end --->>>")

    def setUp(self):
        print("test case start --->")

    def tearDown(self):
        print("test case end --->")

    def test_case(self):
        print("test case1")

    def test_case2(self):
        print("test case2")


if __name__ == '__main__':
    unittest.main()