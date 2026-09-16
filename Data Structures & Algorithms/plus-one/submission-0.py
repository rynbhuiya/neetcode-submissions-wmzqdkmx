class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)


        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + carry
            carry = 1 if num >= 10 else 0
            num = num % 10
            digits[i] = num
        
        if carry:
            digits.insert(0, carry)
        return digits