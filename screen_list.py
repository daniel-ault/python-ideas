#!/bin/python

import time
import curses
from curses import wrapper

class ScreenList:
	_list = None
	_screen = None
	_name = ""
	
	cursor_pos = 0
	screen_pos = {'x': 3, 'y': 3}

	def __init__(self, screen, name, clist):
		self._screen = screen
		self._list = clist
		self._name = name


	def __str__(self):
		return self._name	
	
	
	def _addstr(self, string, mode=curses.A_NORMAL):
		self._screen.addstr(string, mode)
		
	def _addstr(self, y, x, string, mode=curses.A_NORMAL):
		self._screen.addstr(self.screen_pos['y']+y, 
					      self.screen_pos['x']+x,
					      string,
					      mode)
	
	def _move(self, y, x):
		self._screen.move(y,x)


	
	def get_item(self, index):
		if index < 0: return "index cannot be less than 0"
		if index >= len(self._list): return "index cannot be greater than length of list"
		return self._list[index]

	def set_item(self, index, item):
		self._list[index] = item


	def get_list(self):
		return self._list
	
	def set_list(self, l):
		self._list = l


	def draw_list(self, selected_item=-1):
		self._screen.clear()
		mode = curses.A_NORMAL
		i = 0

		for item in self._list:
			if i == selected_item:
				mode = curses.A_STANDOUT
			s = " * {}".format(item)
			self._addstr(i, 0, s, mode)	
			i = i + 1
			mode = curses.A_NORMAL
		self._screen.refresh()
	
	
	def _press_enter(self, cursor_pos):
		if isinstance(self._list[cursor_pos], ScreenList):
			self._list[cursor_pos].run()


	def run(self):
		#self._screen = screen_1
		curses.curs_set(False)
		
		cursor_pos = 0
		self.draw_list(cursor_pos)
		
		while True:
			char = self._screen.getch()
			if char == ord('q'): 
				break
			elif char == curses.KEY_ENTER or char == 10 or char == 13:
				self._press_enter(cursor_pos)

			elif char == curses.KEY_DOWN:
				cursor_pos = cursor_pos + 1
			elif char == curses.KEY_UP:
				cursor_pos = cursor_pos - 1

			
			if cursor_pos < 0: cursor_pos = 0
			elif cursor_pos >= len(self._list): cursor_pos = len(self._list)-1        

			self.draw_list(cursor_pos)
	


#def main(screen):
#	clist = List(screen, ["new list", "with more items", "for", "you", "to", "select"])
#	clist.run()

#wrapper(main)

#wrapper(main)

#curses.nocbreak()
#curses.echo()
#screen.keypad(False)

#curses.endwin()
