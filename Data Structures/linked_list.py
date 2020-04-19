""" Challenges:
Draw/model out inserting a new element into a linked list with only one element.

Draw/model out how to traverse through a linked list in order to find a target value.

Draw/model out how to traverse through a linked list in order to find the maximum value in the linked list.

 """
 
 # inserting a new element into a linked list with only one element.
 
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None 
   
class LinkedList:
  def __init__(self):
    self.head = None
    
  def print_list(self):
    temp = self.head
    while (temp):
      print (temp.data)
      temp = temp.next
      
if __name__=='__main__':
  new_list = LinkedList()
  node1 = Node(42)
  new_list.head = Node(42)
  # a single node can be both the head AND the tail
  node1.next = None
  new_list.print_list()
 
#  how to traverse through a linked list in order to find a target value.

"""
- set up linked list with nodes added using .push function which adds each node to the end of the linked list.
- connect each node using .next, determine which node is the head and tail.
- perhaps use a print function? Assuming we may not know the values in the linked list.
- save the values into a variable.
- compare the saved variables with the target value.
- if not found at the end of the linked list, print "not found"
- when it is found, print "found" with the location of the value in the linked list.
"""
# how to traverse through a linked list in order to find the maximum value in the linked list.

"""
- perhaps use a print function? Assuming we may not know the values in the linked list.
- save the head value as a variable.
- as we go through the linked list, compare the currently saved node value to the next node.
- if the new node has a higher value, save that as the new max value.
- when we get to the end of the linked list, print out the max value.
"""