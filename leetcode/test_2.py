# You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# list1 = [1,2,4] list2 = [1,3,4] output = [1,1,2,3,4,4]

# if same value, no need to concern the order from which list

from typing import Optional


class ListNode: 
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def getNext(self):
        return self.next
    
    def setNext(self, next_node):
        self.next = next_node

class Solution: 
    def mergeTwoSortedLists(self, list1: Optional['ListNode'] = None,list2: Optional['ListNode'] = None):
      head = None
      nowNode = None
      #  temporary pointers that traverse list1 and list2, respectively.
      list1Pointer = list1
      list2Pointer = list2
      if list1 == None and list2 == None:
          return head
      if list1 == None:
          return list2
      if list2 == None:
          return list1
      # list1 and list2 are pointers to the head nodes of the two linked lists.
      # list1.value is the value stored in the head node of list1.
      # list2.value is the value stored in the head node of list2.
      if list1.value <= list2.value:
          head = list1Pointer
          list1Pointer = list1Pointer.getNext()
      else:
          head = list2Pointer
          list2Pointer = list2Pointer.getNext()
      nowNode = head;
    
    
    
       

