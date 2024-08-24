#!env/bin/python

from curses import wrapper
import curses
import os
import math

def main(stdscr):
    stdscr.clear()
    stdscr.border()

    for i in range(curses.COLS):
        if i > 0 and i < curses.COLS - 1:
            stdscr.addstr(2, i, '{}'.format("x"))

    stdscr.addstr(1, 1, 'Size: {}x{} |'.format(curses.LINES, curses.COLS))

    stdscr.refresh()
    stdscr.getkey()
wrapper(main)
