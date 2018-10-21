#!/bin/python

import time
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

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


class NewTextbox:
	height, width = 2, 20
	y, x = 4, 1
	text = ""
	_add_row = False
	_screen = None
	_curses_window = None
	_textbox = None
	
	def __init__(self, height, width, y, x, text="", screen=None):
		self.height, self.width, self.y, self.x = height, width, y, x
		self.text = text
		self._screen = screen
		#self._curses_window = curses.newwin(height, width, y, x)
		#self._textbox = Textbox(self._curses_window)
		self.redraw()
	
	def draw_rectangle(self):
		if self._screen is None:
			return
		rectangle(self._screen,
				  self.y-1,
				  self.x-1,
				  self.height + self.y,
				  self.width + self.x)
		self._screen.refresh()

	
	def redraw(self):
		self._curses_window = curses.newwin(self.height, self.width, self.y, self.x)
		self._textbox = Textbox(self._curses_window)
		self._textbox.stripspaces = False
	
	
	def edit(self, text=""):
		if self._screen is None:
			#print("screen needs to be set")
			return
		
		exit = False
		i = 0
		
		while exit == False:
			
			self.redraw()
			for c in self.text:
				self._textbox.do_command(c)
			#if self._add_row == True:
			#	self._textbox.do_command(chr(16))
			#	self._add_row = False
			self.draw_rectangle()
			self._textbox.edit(self.enter_is_terminate)
			self.text = self._textbox.gather()
			if self._add_row == True:
				self.add_row()
			
			i = i+1
			if i==3: exit = True
			

			
	def enter_is_terminate(self, c):
		if c ==10:
			self.add_row = True
			self.height = self.height + 1
			return 7
		return c
	
	def add_row(self):
		self.height = self.height + 1
		#self.text = self.text + chr(16)
		#self._add_row = False


def main(screen):
	tb = NewTextbox(1,20, 4,1, "text ", screen)
	tb.edit()
	
	
	

def main3(screen):
	ch = screen.getch(); 
	print("KEY NAME : {} - {}\n".format(curses.keyname(ch),ch));
	time.sleep(2)

def main4(screen):
	curses.curs_set(False)
	cursor_pos = 0

	screen.addstr(1,1,"Enter a text or something yo")

	height, width, y, x = 1, 20, 4, 1

	editwin = curses.newwin(height, width, y, x)
	
	curses.curs_set(True)
	rectangle(screen, y-1, x-1, height+y, width+x)
	screen.refresh()
	
	box = Textbox(editwin)
	
	for c in 'test input':
		box.do_command(c)
	
	box.edit(enter_is_terminate)
	
	message = box.gather()
	
	#screen.refresh()
	#screen.move(y,x)
	
	editwin = curses.newwin(height, width, y, x)
	
	curses.curs_set(True)
	rectangle(screen, y-1, x-1, height+y, width+x)
	screen.refresh()
	box = Textbox(editwin)
	
	for c in message:
		box.do_command(c)
	
	box.edit(enter_is_terminate)

	curses.curs_set(False)
	

def enter_is_terminate(c):
	if c == 10:
		return 7
	return c
	

def main2(screen):
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
