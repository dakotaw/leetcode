# Write a function to delete a node (except the tail) in a singly linked list, 
# given only access to that node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node = node.next.copy()