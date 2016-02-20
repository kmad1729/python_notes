#!/usr/bin/env python

def exendList_incorrect(n, l = []):
    'funny implementation of extendList'
    l.append(n)
    return l

list1 = exendList_incorrect(43)
list2 = exendList_incorrect(13, [])
list3 = exendList_incorrect(-12)

print("list1 --> ", list1)
print("list2 --> ", list2)
print("list3 --> ", list3)
