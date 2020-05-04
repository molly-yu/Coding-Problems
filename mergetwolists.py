# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the first two lists.
# Solution by Molly Yu

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First Solution (Iterative)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode() 
        head = l3
        while l1 and l2: # while l2, l1 both non-empty
            if l1.val <= l2.val: #add the smaller value to l3, go to next value in l1/l2
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1: # if, for example, one list is longer than the other, append to l3
            l3.next = l1
        else:
            l3.next = l2
        
        return head.next # return list, which starts at head.next instead of head

    #Testing

    # l1 = ListNode()
    # l2 = ListNode()
    # l1.val = 1
    # second = ListNode()
    # l1.next = second
    # second.val = 2
    # third = ListNode()
    # second.next = third
    # third.val = 3
    
    # l2.val = 1
    # secondd = ListNode()
    # l2.next = secondd
    # secondd.val = 3
    # thirdd = ListNode()
    # secondd.next = thirdd
    # thirdd.val = 4
    
    # mergeTwoLists(1,l1,l2)