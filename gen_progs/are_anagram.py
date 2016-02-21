#!/usr/bin/env python3

from collections import Counter

def are_anagrams(*args):
    'return True if args are anagrams'
    if len(args) < 2:
        raise TypeError("expected 2 or more arguments")
    c = Counter(args[0])
    return all(c == Counter(a) for a in args[1:])

arg1 = "appel apple aplep leapp".split()
#print("check if {} are anagrams".format(arg1))
print("are_anagrams {} ?  {} ".format(arg1, are_anagrams(*arg1)))


