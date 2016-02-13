#!/usr/bin/env python3

from curses import wrapper

def main(stdscr):
    stdscr.clear()

    for i in range(11):
        v = i - 10
        stdscr.addstr(i, 0, '10 multiplied by {} is {}'.format(v, 10 * v))

    stdscr.addstr(23, 33,  "hahhaah")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
