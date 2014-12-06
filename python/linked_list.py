class Node:
	def __init__(self):
		self.data = None
		self.next = None
		

class Linked_list:

	def __init__(self):
		self.cur_node = None
		self.head = None
		self.size = 0
		
	def iterate(self):
		if self.cur_node.next != None:
			self.cur_node = self.cur_node.next
		else:
			self.cur_node = None
	
	def get_head(self):
		return self.head
	
	def add_node(self,data):
		self.size += 1
		node = Node()
		node.data = data
		
		if self.cur_node == None:
			node.next = None
			self.cur_node = node
		else :
			node.next = self.cur_node.next
			self.cur_node.next = node
			self.iterate()	
		if self.head == None:
			self.head = node
			
	def add_node_head(self,data):
		self.size += 1
		node = Node()
		node.data = data
		node.next = self.head
		self.head = node
	
	def list_print(self):
		node = self.head
		while node:
			print node.data
			node = node.next	
	
	def get_size(self):
		return self.size
		
	def is_empty(self):
		if self.get_size() == 0:
			return True
		else:
			return False
	
	def get_current_data(self):
		if self.is_empty or self.cur_node == None:
			return None
		else:
			return self.cur_node.data
		
	def search_node(self, data):
		if self.is_empty():
			return None
		
		self.cur_node = self.head
		
		while self.cur_node:
			if self.cur_node.data == data:
				return self.cur_node
			else:
				self.iterate()
		
	
	def delete_node(self,data):
		node = self.search_node(data)
		if node != None:
			if node == self.head:
				self.head = node.next
				self.size -= 1
			else :
				self.cur_node = self.head
				while self.cur_node:
					if self.cur_node.next.data == data:
						self.cur_node.next = self.cur_node.next.next
						self.size -= 1
						return
					else:
						self.iterate()
		

'''2
l = Linked_list()

l.add_node_head(1)
l.add_node_head(2)
l.add_node_head(3)
l.add_node_head(4)
l.add_node_head(5)

print "a"
l.list_print()
'''





