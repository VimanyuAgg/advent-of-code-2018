# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

import sys
sys.path.append("..")

import pandas as pd

from d2 import inventory_management_system_part1, inventory_management_system_part2

class TestInventoryManagementSystem (unittest.TestCase):

    def test_part1_ex1(self):
        input_list = ["abcdef",
                      "bababc",
                      "abbcde",
                      "abcccd",
                      "aabcdd",
                      "abcdee",
                      "ababab"]

        actual = inventory_management_system_part1(input_list)
        expected = 12
        self.assertEqual(actual,expected)


    def test_part1_final(self):
        df = pd.read_csv('d2_input', header=None)

        flatten_list = df.values.flatten()
        input_list = list(flatten_list)

        actual = inventory_management_system_part1(input_list)
        # print("****")
        # print(actual)
        # print("********")

    def test_part2_ex1(self):
        input_list = ["abcde",
                      "fghij",
                      "klmno",
                      "pqrst",
                      "fguij",
                      "axcye",
                      "wvxyz"]

        actual = inventory_management_system_part2(input_list)
        expected = 'fgij'
        self.assertEqual(actual,expected)


    def test_part2_final(self):
        df = pd.read_csv('d2_input', header=None)

        flatten_list = df.values.flatten()
        input_list = list(flatten_list)

        actual = inventory_management_system_part2(input_list)
        print("****")
        print(actual)
        print("*****")





if __name__ == "__main__":
    unittest.main()
