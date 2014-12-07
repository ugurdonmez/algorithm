# execfile("./linked_list.py")

from linked_list import Linked_list

class Stack:
	def __init__(self):
		self.list = Linked_list()
		self.size = 0
	
	def push(self,data):
		self.list.add_node_head(data)
		self.size += 1
	
	def pop(self):
		if self.isEmpty:
			return None
		else :
			self.size -= 1
			data = self.top()
			self.list.delete_node(data)
			return data
			
	
	def top(self):
		if self.isEmpty:
			return None
		else:
			return self.list.get_head.data
	
	def isEmpty(self):
		if self.size == 0:
			return True
		else:
			return False
			

'''
s = Stack()

l = Linked_list()

l.add_node_head(1)
l.add_node_head(2)
l.add_node_head(3)
l.add_node_head(4)
l.add_node_head(5)

print "a"
l.list_print()
'''