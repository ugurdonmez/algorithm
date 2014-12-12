class Node:
   def __init__(self):
      self.data = None
      self.left = None
      self.right = None
      self.parent = None
      self.color = 0 # red


class RedBlackTree:
   def __init__(self):
      self.root = None
   
   
   def getGrandParent(self,n):
      if n != None and n.parent != None:
         return n.parent.parent
      else:
         return None
      
   def getUncle(self,n):
      g = self.getGrandParent(n)
      
      if g == None:
         return None
      else:
         if n.parent == g.left:
            return g.right
         else:
            return g.left
         
   def addNode(self,parent,node,value):
      if self.root == None:
         self.root = Node()
         self.root.left = self.root.right = self.root.parent = None
         self.root.color = 0
         return self.root
      elif node == null:
         n = Node()
         n.data = bvalue
         n.left = n.right = None
         n.parent = parent
         n.color = 0
         return n
      else:
         if node.data > value:
            return addNode(node,node.left,value)
         else:
            return addNode(node,node.right,value)
         
   def insertCase1(self,node):
      