class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            if num in dct: 
                return True
            dct[num] = 0
        return False