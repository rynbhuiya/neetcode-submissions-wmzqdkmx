# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None

        ret = lists[0]
        for i in range(1, len(lists)):
            ret = self.mergeTwoLists(ret, lists[i])
        
        return ret
    

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = None

        head = None
        while curr1 and curr2:
            if head is None:
                if curr1.val < curr2.val:
                    res = curr1
                    head = res
                    curr1 = curr1.next
                else:
                    res = curr2
                    head = res
                    curr2 = curr2.next
                continue

            if curr1.val < curr2.val:
                head.next = curr1
                head = curr1
                curr1 = curr1.next
            else:
                head.next = curr2
                head = curr2
                curr2 = curr2.next
        
        while curr1:
            if head is None:
                res = curr1
                head = curr1
                curr1 = curr1.next
                continue
            head.next = curr1
            head = curr1
            curr1 = curr1.next
        
        while curr2:
            if head is None:
                res = curr2
                head = curr2
                curr2 = curr2.next
                continue
            head.next = curr2
            head = curr2
            curr2 = curr2.next

        return res