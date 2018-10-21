#!/bin/python

import time
import curses
from curses import wrapper

from screen_list import List

def main(screen):
	l1 = ["nother", "teest", "list", "full", "of", "items", "for", "me", "to", "select"]
	l2 = ["hi", "i", "like", "you"]
	l3 = ["ope", "let", "me", "just", "sneak", "right", "past", "ya"]

	clist1 = List(screen, "List1", l1)
	clist2 = List(screen, "List 2", l2)
	clist3 = List(screen, "lol", l3)

	l4 = [clist1, clist2, clist3]
	clist4 = List(screen, "Master List", l4)
	
	#print(isinstance(clist4.get_item(2), List))
	#time.sleep(2)

	#clist1.run()
	#clist2.run()
	#clist3.run()
	clist4.run()
	

	#clist = List(screen, "i am a list", l)
	#print(clist)
	
	#time.sleep(2)

wrapper(main)
