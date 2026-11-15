# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtyp12e: Optional[ListNode]
        """
        final= ListNode(0)
        current = final
        while list1 and list2:
            if list1.val <=list2.val:
                current.next = list1
                current=current.next
                list1=list1.next
            else:
                current.next = list2
                current=current.next
                list2=list2.next
        while list1:
            current.next=list1
            current=current.next
            list1=list1.next
        while list2:
            current.next=list2
            current=current.next
            list2=list2.next
        return final.next
        
        
        
        
        