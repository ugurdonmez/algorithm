class Heap:
   def __init__(self):
      self.array = []
      self.size = 0
   
      
   def heapify(self,pos): #create a heap out of given array of elements
      l = 2 * pos
      r = 2 * pos + 1
      
      largest = pos
      
      if l < self.size and self.array[l] > self.array[largest]:
         largest = l
      
      if r <= self.size and self.array[r] > self.array[largest]:
         largest = r
         
      if largest != pos:
         temp = self.array[largest]
         self.array[largest] = self.array[pos]
         self.array[pos] = temp
         self.heapify(largest)
    
   def find_max(self):
      if self.isEmpty():
         return None
      else:
         return self.array[0]
      
   def delete_max(self):
      data = self.array[0]
      self.array[0] = self.array[self.size-1]
      self.size -= 1
      self.heapify(0)
      
   def shift_up(self,pos):
      while pos > 0 and self.array[ pos / 2 ] < self.array[pos]:
         temp = self.array[pos / 2]
         self.array[pos / 2] = self.array[pos]
         self.array[pos] = temp
         pos = pos / 2
        
   def insert(self, data):
      self.array.append(data)
      self.size += 1
      self.shift_up(self.size -1)
      
      
   def get_size(self):
      return self.size
   
   def isEmpty(self):
      if self.size == 0:
         return True
      else :
         return False

'''
heap = Heap()
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(9)
heap.insert(3)
heap.insert(2)
print heap.isEmpty()


print heap.find_max()
print heap.get_size()


heap.delete_max()

print heap.isEmpty()


print heap.find_max()
print heap.get_size()
'''














