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
      if self.isEmpty():
         return None
      else :
         data = self.top()
         self.list.delete_node(data)
         self.size -= 1
         return data

   def top(self):
      if self.isEmpty():
         return None
      else:
         return self.list.get_head().data

   def isEmpty(self):
      if self.size == 0:
         return True
      else:
         return False



'''
s = Stack()


s.push(1)

s.push(2)

print s.pop()
print s.pop()


print s.isEmpty()
'''