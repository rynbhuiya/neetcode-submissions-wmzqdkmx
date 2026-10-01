class Solution:
    def hammingWeight(self, n: int) -> int:
        res = format(n, 'b')
        count = 0
        for c in res:
            if c == '1':
                count += 1
        return count