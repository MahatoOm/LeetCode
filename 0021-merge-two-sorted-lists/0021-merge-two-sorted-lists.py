# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:    

        node = ListNode()
        root = node
        while list1 or list2:

            if list1 and list2:
                if list1.val < list2.val:
                    root.next = ListNode(list1.val)
                    root = root.next
                    list1 = list1.next
                else:
                    root.next = ListNode(list2.val)
                    root = root.next
                    list2 = list2.next

            elif list1:
                root.next = ListNode(list1.val)
                root = root.next
                list1 = list1.next
            elif list2:
                root.next = ListNode(list2.val)
                root = root.next
                list2 = list2.next

        return node.next 