# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

import sys
sys.path.append("..")

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



if __name__ == "__main__":
    unittest.main()
