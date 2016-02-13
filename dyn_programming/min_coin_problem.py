#!/usr/bin/env python
'given a bag of infinite different valued coins check if a change exists'

import unittest

def is_change_possible(possible_coin_vals, target_sum):
    res_arr = [False] * (target_sum + 1)
    res_arr[0] = True
    for i in range(1, len(res_arr)):
        for c in possible_coin_vals:
            if i - c >=0:
                if(res_arr[i - c]):
                    res_arr[i] = True
                    break
    return res_arr[target_sum]

class TestChangePossible(unittest.TestCase):


    def test_is_change_possible(self):
        self.assertTrue(is_change_possible([2], 2))
        self.assertFalse(is_change_possible([2], 1))
        self.assertFalse(is_change_possible([2], 3))
        self.assertTrue(is_change_possible([2], 4))
        self.assertTrue(is_change_possible([2], 110))
        self.assertFalse(is_change_possible([2], 5))
        self.assertFalse(is_change_possible([2], 10000000000000))
        self.assertTrue(is_change_possible([3, 7], 10))
        self.assertFalse(is_change_possible([3, 7], 11))
        self.assertFalse(is_change_possible([3, 7], 8))
        self.assertTrue(is_change_possible([3, 7], 9))

if __name__ == "__main__":
    unittest.main()
