#!/usr/bin/env python3

from curses import wrapper
import curses

def main(stdscr):
    stdscr.clear()

    i = 0
    while True:
        c = stdscr.getch()
        stdscr.refresh()
        if c == ord('p'):
            stdscr.addstr(0, 23, 'print command issued')
        elif c == ord('q'):
            stdscr.addstr(0, quitting)
        elif c == curses.KEY_HOME:
            x = y = 0
        else:
            stdscr.addstr(i, 23, "you typed {:c}".format(c))
        i += 1

wrapper(main)
