#!/bin/python

import mysql.connector
import time
import curses
from curses import wrapper
from screen_list import ScreenList


def main(screen):
	mydb = mysql.connector.connect(
			host='blackboi',
			user='python',
			password='',
			database='ideas'
		)

	mycursor = mydb.cursor()

	mycursor.execute('select distinct category from idea;')
	categories = mycursor.fetchall()
	categories = [category for category, in categories]

	master_list = ScreenList(screen, "Master List", categories)
	
	for i, category in enumerate(categories):
		query = "select title from idea where category = '{}'".format(category)
		mycursor.execute(query)
		items = mycursor.fetchall()
		items = [item for item, in items]
		master_list.set_item(i, ScreenList(screen, category, items))
	
	master_list.run()

wrapper(main)