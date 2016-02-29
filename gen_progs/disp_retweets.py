#!/usr/bin/env python3

'''Display the number of retweets a tweet gets using 4 characters total with 
max one position past the decimal point in US and Indonesian standard 
(eg 1.5 b, 3.2k)

100 -> 100
1000 -> 1k
9999 -> 9.9k
10,000 -> 10k
50,000 -> 50k
99,999 -> 99.9k
100,000 -> 100k
500,000 -> 500k
999,999 -> 999k
1,000,000 -> 1m
10,000,000 -> 10m
100,000,000 -> 100m
1,000,000,000 -> 1b
1,000,000,000,000 -> Not Yet implemented!
'''


def get_tweet_disp(inp_num):
    out_list = "{:,}".format(inp_num).split(',')
    len_out_list = len(out_list)
    if len_out_list == 1:
        return ''.join(out_list)
    elif len_out_list == 2:
        #thousands
        suff = 'k'
    elif len_out_list == 3:
        #millions
        suff = 'm'
    elif len_out_list == 4:
        #billions
        suff = 'b'
    else:
        raise Exception("not yet implemented")

    return out_list[0] + '.' + out_list[1][0] + suff

inp_outp_map = {
        100: '100',
        1000: '1k',
        9999: '9.9k',
        10000: '10k',
        50000: '50k',
        99999: '99.9k',
        100000: '100k',
        500000: '500k',
        999999: '999k',
        1000000: '1m',
        10000000: '10m',
        100000000: '100m',
        1000000000: '1b',
        10000000000: '10b',
        100000000000: '100b',
        #1000000000000: '100b',
        }

for inp, outp in inp_outp_map.items():
    print("outp for {} --> {};\nexpected --> {}".format(inp, 
        get_tweet_disp(inp), outp))
