class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)): 
            to_add = target - nums[i]
            if to_add in hash_map.keys():
                return [hash_map[to_add], i]
            else:
                hash_map[nums[i]] = i
        