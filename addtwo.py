class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while True: 
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next
            # current.val += carry  
            carry = current.val//10
            current.val = current.val%10
            if l1 or l2 or carry:
                current.next = ListNode(carry)
                current = current.next
            else: break 
        return  dummy
