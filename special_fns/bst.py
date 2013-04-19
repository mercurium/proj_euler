

class bst():
  def __init__(self,head=None,left=None,right=None):
    self.head = head
    self.left = left
    self.right = right
    self.numNodes = 1 if head!=None else 0
  
  def find(self,value):
    if not self.head:
      return False
    if self.head == value:
      return True
    elif self.head > value:
      if not self.left:
        return False
      return self.left.find(value)
    else:
      if not self.right:
        return False
      return self.right.find(value)
  
  def insert(self,value):
    self.numNodes+=1
    if not self.head:
      self.head = value
    elif self.head > value:
      if not self.left:
        self.left = bst(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = bst(value)
      else:
        self.right.insert(value)
  
  def median(self):
    i = self.numNodes
    if i == 0: return "Wrong!"
    if i == 1: return self.head
    if i % 2 == 1:
      return self.nth_node(i//2)
    val = (self.nth_node(i//2)+self.nth_node(i//2-1))/2.
    if val % 1 == 0:
      return int(val)
    return val
  
  def nth_node(self,n):
    if self.left != None and self.right != None:
      i,j = self.left.numNodes,self.right.numNodes
      if n == i:
        return self.head
      elif n < i:
        return self.left.nth_node(n)
      else:
        return self.right.nth_node(n-i-1)
    elif self.left == None:
      if n == 0:
        return self.head
      return self.right.nth_node(n-1)
    elif self.right == None:
      if n == self.numNodes-1:
        return self.head
      return self.left.nth_node(n)
    else:
      return self.head
  
  def add(self,value):
    self.insert(value)
  
  def delete(self,value):
    if not self.find(value):
      return False
    self.delete_h(value)
    return True
    
  def delete_h(self,value):
    self.numNodes -=1
    if value == self.head:
      #if we have a tree of size 1...
      if not self.left and not self.right:
        self.head =None
      #if left side is not defined, we can just make the right the head
      elif not self.left:
        self.head = self.right.head
        self.left = self.right.left
        self.right = self.right.right
      #if the right side is not defined, we can just make the left the head
      elif not self.right:
        self.head = self.left.head
        self.right = self.left.right
        self.left = self.left.left
      #if both have values...
      elif self.right.numNodes > self.left.numNodes:
        node =self.right
        next =self.right.left
        node.numNodes -=1
        if not next:
          self.head = node.head
          self.right = node.right
          return
        while next.left:
          node = next
          next = next.left
          node.numNodes -=1
        self.head = next.head
        node.left = next.right
      elif self.right.numNodes <= self.left.numNodes:
        node =self.left
        next =self.left.right
        node.numNodes -=1
        if not next:
          self.head = node.head
          self.left = node.left
          return
        while next.right:
          node = next
          next = next.right
          node.numNodes -=1
        self.head = next.head
        node.right = next.left
        
    elif self.head > value:
      a = self.left.delete_h(value)
    else:
      a = self.right.delete_h(value)
    return
      
  def printTree(self):
    print self.printTrees()
    
  def printTrees(self):
    if self.head == None: return []
    r = [self.right.printTrees()] if self.right != None and self.right.head !=None else []
    l = [self.left.printTrees()] if self.left != None and self.left.head !=None else []
    return l + [self.head]+ r







