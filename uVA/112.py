import re
from sys import stdin

class Node:
  def __init__(self):
    self.left = None
    self.right = None
    self.has_value = False
    self.value = None

def tree_from_s_expr(source):
  number_or_symbol = re.compile('(-*\d+|[^ 0-9\n])')
  root = None
  target = None
  nodes = []
  tokens = re.findall(number_or_symbol, source) #will find the symbols stored in variable "number of symbol" from the "source" variable
  for token in tokens:
    #for each start parentesis "(" instantiate a Node class object
    if token == "(":
      n = Node()  #object of Node class initialized with default value. 
      if len(nodes) > 0:
        
        if nodes[-1].left == None: 
          nodes[-1].left = n #if the left child of the tree is None then add the next object(another tree) to the left node else to the right node

        else:
          nodes[-1].right = n
          
      else:
        root = n
      nodes.append(n)
      #print(nodes)
      
    elif token == ")":
      nodes.pop()
      if len(nodes) == 0:
        yield target, root
        root = None
        target = None
        
    else:
      if len(nodes) == 0:
        target = int(token)
        
      else:
        nodes[-1].value = int(token)
        nodes[-1].has_value = True
  return

def sum_path_exists(root, current, target):
  total = current
  if not root:
    return False
  if root.has_value:
    total += root.value
    
    # if leaf
    if root.left.has_value == root.right.has_value == False:
      return total == target
    
    if sum_path_exists(root.left, total, target):
      return True
    return sum_path_exists(root.right, total, target)
    

inp = "".join([l for l in stdin])
for target, root in tree_from_s_expr(inp):
  if sum_path_exists(root,0,target) == True:
    print("yes")
  else:
    print("no")

