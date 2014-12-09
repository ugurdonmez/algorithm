nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
   'B': {'A': 5, 'D': 1, 'G': 2},
   'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
   'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
   'G': {'B': 2, 'D': 1, 'C': 2},
   'C': {'G': 2, 'E': 1, 'F': 16},
   'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
   'F': {'A': 5, 'E': 2, 'C': 16}}


def visit(node):
   print "visit " + str(node)

visited = []

def dft(node):
   visited.append(node)
   visit(node)
   
   # for all adj v
   distance = distances[node]
   for key in distance.keys():
      if key not in visited:
         dft(key)

dft(nodes[0])