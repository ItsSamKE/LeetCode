# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Linked lists are like a lesser-known cousin of lists
# Each element of a linked list is called a node, and every node has two different fields: Data & Next
# 1. Data contains the value to be stored in the node.
# 2. Next contains a reference to the next node on the list.
# Reference: https://realpython.com/linked-lists-python/
class Solution:
    def mergeTwoLists(self, list1, list2):

        NewList = list1 + list2
        return NewList.sort()


sol = Solution()
print(sol.mergeTwoLists([1, 2, 4], [1, 3, 4]))
