import datetime


class IdeaItem:
	title = ""
	category = ""
	description = ""
	todo_list = []

	def __init__(self, title, category, description):
		self.title = title
		self.category = category
		self.description = description
	
	def __str__(self):
		return("title: {}  cat: {}  descr: {}".format(
				self.title, self.category, self.description))
	
	def __repr__(self):
		return (
		'title       : {}\n'
		'category    : {}\n'
		'description : {}\n'
		'todo_list   : {}\n'
		).format(
		self.title,
		self.category,
		self.description,
		str(self.todo_list))

	#TODO - throw exception if out of index?

	def complete_todo(self, index):
		if index > 0 and index < len(self.todo_list):
			self.todo_list[index].complete()
	
	def uncomplete_todo(self, index):
		if index > 0 and index < len(self.todo_list):
			self.todo_list[index].uncomplete()

	def add_todo(self, title, description):
		self.todo_list.append(TodoItem(title, description))
	
	def add_todo_obj(self, todo):
		if isinstance(todo, TodoItem):
			self.todo_list.append(todo)
	
	def get_todo(self, index):
		if index > 0 and index < len(self.todo_list):
			return self.todo_list[index]
		else:
			return None

	@staticmethod
	def test():
		item = IdeaItem("idea title", "animals", "this is just a test okay")
		item.add_todo("test todo", "test description for todo")
		item.add_todo("nother todo", "description")
		item.add_todo_obj(TodoItem("test", "obj"))
		item.complete_todo(1)
		item.complete_todo(2)
		item.uncomplete_todo(1)
		print("\nstr : \n" + str(item))
		print("\nrepr : \n" + repr(item) + "\n")



class TodoItem:
	completed = False
	completed_date = None
	title = ""
	description = ""

	def __init__(self, title, description):
		self.title = title
		self.description = description
	
	def __str__(self):
		if self.title.strip() == "" and self.description.strip() == "":
			return "TodoItem has no title or description"
		else:
			return self.title.strip() + " : " + self.description.strip()
	
	def __repr__(self):
		return (
		'\ntitle          : {}\n'
		'description    : {}\n'
		'completed      : {}\n'
		'completed_date : {}\n'
		).format(
		self.title,
		self.description,
		self.completed,
		self.completed_date)

	def complete(self):
		self.completed = True
		self.completed_date = datetime.datetime.now()

	def uncomplete(self):
		self.completed = False
		self.completed_date = None

	@staticmethod
	def test():
		item = TodoItem("test", "descr")
		print("\nstr : \n" + str(item) + "\n")
		print("repr : \n" + repr(item))
		item.complete()
		print("\nrepr (after completing) : \n" + repr(item))
		item.uncomplete()
		print("\nrepr (after uncompleting) :\n" + repr(item) + "\n")



def test():
	idea = IdeaItem("this is idea", "test item", "this is a test idea")

	#print("title     : " + idea.title)
	#print("category  : " + idea.category)
	#print("descr     : " + idea.description)

	#idea.add_todo("test todo", "this is a test")

	#print("todo_list : " + idea.todo_list)



IdeaItem.test()
