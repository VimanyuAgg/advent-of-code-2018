# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import pandas as pd
import sys
sys.path.append("..")

from d1 import chronal_calibration_part1 ,chronal_calibration_part2


class TestChronalCalibration(unittest.TestCase):

    def test_part1_ex1(self):
        actual = chronal_calibration_part1([+1, -2, +3, +1])
        expected = 3
        self.assertEqual(actual, expected)

    def test_part1_ex2(self):
        actual = chronal_calibration_part1([+1, +1, +1])
        expected = 3
        self.assertEqual(actual, expected)


    def test_part1_ex3(self):
        actual = chronal_calibration_part1([+1, +1, -2])
        expected = 0
        self.assertEqual(actual, expected)

    def test_part1_ex4(self):
        actual = chronal_calibration_part1([-1, -2, -3])
        expected = -6
        self.assertEqual(actual, expected)

    #
    def test_part1_final(self):
        df = pd.read_csv('d1_test_input', header=None)
        flatten_list = df.values.flatten()
        list_df = list(flatten_list)
        list_df = [int(i) for i in list_df]
        # print(list_df)
        actual = chronal_calibration_part1(list_df)
        # print("*******")
        # print(actual)
        # print("*******")

    def test_part2_ex1(self):
        actual = chronal_calibration_part2([+1, -2, +3, +1])
        expected = 2
        self.assertEqual(actual, expected)

    def test_part2_ex2(self):
        actual = chronal_calibration_part2([+1, -1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_part2_ex3(self):
        actual = chronal_calibration_part2([-6, +3, +8, +5, -6])
        expected = 5
        self.assertEqual(actual, expected)

    def test_part2_ex4(self):
        actual = chronal_calibration_part2([+7, +7, -2, -7, -4])
        expected = 14
        self.assertEqual(actual, expected)

    def test_part2_ex5(self):
        actual = chronal_calibration_part2([+3, +3, +4, -2, -4])
        expected = 10
        self.assertEqual(actual, expected)

    def test_part2_final(self):
        df = pd.read_csv('d1_test_input', header=None)
        flatten_list = df.values.flatten()
        list_df = list(flatten_list)
        list_df = [int(i) for i in list_df]
        print(list_df)
        actual = chronal_calibration_part2(list_df)
        print("*******")
        print(actual)
        print("*******")





if __name__ == "__main__":
    unittest.main()
