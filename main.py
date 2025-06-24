#!/usr/bin/env python

from curses import wrapper
import curses
from time import sleep


def seperator(scr, row):
    for i in range(curses.COLS):
        if i > 0 and i < curses.COLS - 1:
            scr.addstr(row, i, "{}".format("x"))


def main(stdscr):
    should_exit = False

    stdscr.clear()
    stdscr.border()
    curses.curs_set(0)

    stdscr.addstr(1, 1, "Size: {}x{}".format(curses.LINES, curses.COLS))
    seperator(stdscr, 2)

    kb_input = stdscr.getkey()

    while should_exit == False:
        match kb_input:
            case "q":
                should_exit = True
            case _:
                should_exit = False

        stdscr.addstr(curses.LINES - 1, 1, kb_input)
        stdscr.refresh()
        sleep(2)


wrapper(main)
