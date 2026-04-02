class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hist = set([])
        for val in nums:
            if val in hist:
                return True
            else:
                hist.add(val)

        return False