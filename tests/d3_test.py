# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import pandas as pd
import sys
sys.path.append("..")

from d3 import no_matter_how_you_slice_it_part1, no_matter_how_you_slice_it_part2

class TestNoMatterHowYouSliceIt(unittest.TestCase):
    #
    def test_part1_ex1(self):
        input_list = ['# 1 @ 1,3: 4x4',
                      '#2 @ 3,1: 4x4',
                      '#3 @ 5,5: 2x2']

        actual = no_matter_how_you_slice_it_part1(input_list)
        expected = 4
        self.assertEqual(actual,expected)

    def test_part1_final(self):
        reader = open('d3_input')
        input_list = []
        for line in reader:
            input_list.append(line)

        # print(input_list)
        actual = no_matter_how_you_slice_it_part1(input_list)
        # print("***")
        # print(actual)
        # print("****")

    def test_part2_ex1(self):
        input_list = ['# 1 @ 1,3: 4x4',
                      '#2 @ 3,1: 4x4',
                      '#3 @ 5,5: 2x2']

        actual = no_matter_how_you_slice_it_part2(input_list)
        expected = 3
        self.assertEqual(actual, expected)

    def test_part2_final(self):
        reader = open('d3_input')
        input_list = []
        for line in reader:
            input_list.append(line)

        # print(input_list)
        actual = no_matter_how_you_slice_it_part2(input_list)
        print("***")
        print(actual)
        print("****")

if __name__ == "__main__":
    unittest.main()