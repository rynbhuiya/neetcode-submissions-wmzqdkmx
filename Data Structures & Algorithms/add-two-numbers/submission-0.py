# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        ret = None
        res = None
        carry = 0 

        while curr1 and curr2:
            total = curr1.val + curr2.val + carry
            if total >= 10:
                carry = 1
            else:
                carry = 0
            total = total % 10

            temp = ListNode(total)

            if ret is None:
                ret = temp
                res = ret
            else:
                res.next = temp
                res = temp

            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            total = curr1.val + carry
            carry = 1 if total >= 10 else 0
            total = total % 10

            temp = ListNode(total)
            res.next = temp
            res = temp

            curr1 = curr1.next

        while curr2:
            total = curr2.val + carry
            carry = 1 if total >= 10 else 0
            total = total % 10

            temp = ListNode(total)
            res.next = temp
            res = temp

            curr2 = curr2.next
        
        if carry:
            temp = ListNode(1, None)
            res.next = temp
        else:
            res.next = None
        
        return ret

        

        

            


            

            
