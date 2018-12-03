# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append("..")

from d3 import no_matter_how_you_slice_it_part1, no_matter_how_you_slice_it_part2

class TestNoMatterHowYouSliceIt(unittest.TestCase):

    def test_part1_ex1(self):
        input_list = ['# 1 @ 1,3: 4x4',
                      '#2 @ 3,1: 4x4',
                      '#3 @ 5,5: 2x2']

        actual = no_matter_how_you_slice_it_part1(input_list)
        expected = 4
        self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()