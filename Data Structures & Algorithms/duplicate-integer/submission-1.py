class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for el in nums:
            if hash_table.get(el):
                return True
            else:
                hash_table[el] = True
        return False