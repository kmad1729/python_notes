#!/usr/bin/env python3

'''Given a number n, give me a function that returns the nth fibonacci number. 
Running time, space complexity, iterative vs. recursive.
'''

def get_nth_fib(n):
    'get nth fibonacci number. n is 1 based'
    assert n > 0

    a, b = 1, 1
    i = 0
    while(i < n - 1):
        a, b = b, a + b
        i += 1
    return a

def _get_suff(i):
    if i == 1:
        return "st"
    elif i == 2:
        return "nd"
    elif i == 3:
        return "rd"
    else:
        return "th"

for i in range(1, 21):
    print("{:2}{} fib number = {}".format(i, _get_suff(i), get_nth_fib(i)))
