# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # optimal carryover approach
    def addTwoNumbers(self, curDigit1: Optional[ListNode], curDigit2: Optional[ListNode]) -> Optional[ListNode]:
        # buffer head node
        reversedSumDigits = curSumDigit = ListNode(-1, None)
        carryOverDigit = 0

        # keep taking sum of digits as long as one number's digits exist
        while curDigit1 or curDigit2:
            digitVal1 = 0 if not curDigit1 else curDigit1.val
            digitVal2 = 0 if not curDigit2 else curDigit2.val
            sumVal = digitVal1 + digitVal2 + carryOverDigit

            # next digit in reversed sum should be last digit of sum value
            # next carry over value should be first digit of sum value
            curSumDigit.next = ListNode(sumVal % 10, None)
            carryOverDigit = sumVal // 10

            # traverse to next (logically previous) digits in both numbers
            curDigit1 = curDigit1.next if curDigit1 else None
            curDigit2 = curDigit2.next if curDigit2 else None
            curSumDigit = curSumDigit.next

        # finally append carry over digit to (logically front of) reversed sum
        # once no more digits to add from both numbers
        if carryOverDigit != 0:
            curSumDigit.next = ListNode(carryOverDigit, None)

        return reversedSumDigits.next
