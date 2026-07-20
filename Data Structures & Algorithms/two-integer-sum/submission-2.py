class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_els = {}

        for curr_num_ind in range(len(nums)):
            
            need_to_find = target - nums[curr_num_ind]

            if need_to_find in prev_els.keys():
                return [prev_els[need_to_find], curr_num_ind]
            else:
                prev_els[nums[curr_num_ind]] = curr_num_ind