from linked_list import Linked_list

class Queue:
   def __init__(self):
      self.list = Linked_list()
      self.size = 0
   
   def poll(self):
      if self.isEmpty():
         return None
      else:
         data = self.peek()
         # linked list should store last element and delete node in O(1)
         self.list.delete_node(data)
         self.size -= 1
         return data

   def peek(self):
      if self.isEmpty():
         return None
      else:
         return self.list.get_head().data

   def add(self,data):
      self.list.add_node(data)
      self.size += 1

   def isEmpty(self):
      if self.size == 0:
         return True
      else:
         return False

'''
q = Queue()

q.add(1)
q.add(2)
q.add(3)

print q.peek()
print q.poll()
print q.peek()
print q.poll()
print q.poll()
print q.poll()
'''