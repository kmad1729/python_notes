#!/usr/bin/env python3

'''Given n sets of choices: (1,2,3), (2,3,4), (4,5) You pick one element from 
each set of choices. Generate all possible picking.
'''

def get_all_choices(inp_list, pref_list):
    if(len(inp_list) == 0):
        print(pref_list)
        return

    curr_set = inp_list[0]
    for elem in curr_set:
        pref_list.append(elem)
        get_all_choices(inp_list[1:], pref_list)
        pref_list.pop()

delim = "*" * 20

l1 = [(1,2), (5,6)]
print("l1 -->", l1)
#output should be (1, 5), (1, 6), (2, 5), (2, 6)
get_all_choices(l1, [])
print(delim)
l1 = [(1,2,3), (2,3,4), (4, 5)]
print("l1 -->", l1)
get_all_choices(l1, [])
