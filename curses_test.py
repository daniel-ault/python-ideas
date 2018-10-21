#!/bin/python

import time
import curses
from curses import wrapper

#screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
#screen.keypad(True)

#for i in range(0,11):
#	screen.addstr(i, 0, 'test string hahaha')

clist = ["item 1", 
         "item2",
		 "nother item",
		 "whoo"]

def main(screen):
	#screen_lines = curses.LINES
	#screen_cols  = curses.COLS
	
	curses.curs_set(False)
	
	cursor_pos = 0

	draw_list(screen, clist, cursor_pos)

	
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		
		elif char == curses.KEY_DOWN:
			cursor_pos = cursor_pos + 1
		
		elif char == curses.KEY_UP:
			cursor_pos = cursor_pos - 1
		
		if cursor_pos < 0: cursor_pos = 0
		elif cursor_pos >= len(clist): cursor_pos = len(clist)-1        

		draw_list(screen, clist, cursor_pos)

	#screen.addstr(0,0, "lines: {} cols: {}".format(screen_lines, screen_cols))
	#screen.addstr("lines: {} cols: {}".format(screen_lines, screen_cols))
	#screen.addstr("lines: {} cols: {}".format(screen_lines, screen_cols), mode)
	
	#time.sleep(2)


def draw_list(screen, clist, selected_item=-1):
	mode = curses.A_NORMAL
	
	i = 0

	for item in clist:
		if i == selected_item:
			mode = curses.A_STANDOUT

		screen.move(i, 0)
		screen.addstr("{}".format(item), mode)	
		i = i + 1
		
		mode = curses.A_NORMAL

	screen.refresh()
	



wrapper(main)

#curses.nocbreak()
#curses.echo()
#screen.keypad(False)

#curses.endwin()
