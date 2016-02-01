#!/usr/bin/env python
'given a bag of infinite different valued coins check if a change exists'

import unittest

def get_max_contiguous_sum(num_list):
    aux_arr = [0] * len(num_list)
    max_at_i = [0] * len(num_list)

    aux_arr[0] = max(0, num_list[0])
    max_at_i[0] = num_list[0]

    for i in range(1, len(num_list)):
        aux_arr[i] = max(aux_arr[i - 1] + num_list[i], 0)
        if(max_at_i[i - 1] < 0):
            max_at_i[i] = max(max_at_i[i - 1], num_list[i])
        else:
            max_at_i[i] = max(max_at_i[i - 1], aux_arr[i])


    return max_at_i[-1]

class TestChangePossible(unittest.TestCase):

    def test_get_max_sum(self):
        self.assertEqual(5, get_max_contiguous_sum([5, -3, -4, -5]))
        self.assertEqual(55, 
                get_max_contiguous_sum([5, 15, -30, 10, -5, 40, 10]))

        self.assertEqual(55, 
                get_max_contiguous_sum([5, 15, -30, 10, -5, 40, 10, -5]))

        self.assertEqual(-4, 
                get_max_contiguous_sum([-23, -5, -4]))

        self.assertEqual(0, 
                get_max_contiguous_sum([-23, -5, -4, 0]))

        self.assertEqual(4, 
                get_max_contiguous_sum([-23, -5, -4, 0, 4]))

        self.assertEqual(4, 
                get_max_contiguous_sum([-23, 4, -5, -4, 0, 4]))

if __name__ == "__main__":
    unittest.main()

