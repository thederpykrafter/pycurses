#!/usr/bin/env python

from time import sleep
import curses


def seperator(screen, row):
    for i in range(curses.COLS):
        if i > 0 and i < curses.COLS - 1:
            screen.addstr(row, i, "{}".format("x"))


def main(stdscr):
    should_exit = False

    while should_exit == False:
        stdscr.clear()
        stdscr.border()
        curses.curs_set(0)

        stdscr.addstr(1, 1, "Size: {}x{}".format(curses.LINES, curses.COLS))
        seperator(stdscr, 2)

        kb_input = stdscr.getkey()

        match kb_input:
            case "q":
                should_exit = True
            case _:
                should_exit = False

        keydisplay = "<" + kb_input + ">"
        stdscr.addstr(curses.LINES - 2, 1, keydisplay)
        stdscr.refresh()
        sleep(0.5)


curses.wrapper(main)
