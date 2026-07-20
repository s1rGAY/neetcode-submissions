class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        mult_left = [1]*len(nums)
        mult_right = [1]*len(nums)

        for index in range(len(nums)):
            print(f'current el : {nums[index]}')

            if index==0:
                mult_left[index] = 1
                    
                for el in nums[index+1:]:
                    mult_right[index]*= el

            elif index==len(nums)-1:
                mult_right[index] = 1

                for el in nums[:index]:
                    mult_left[index]*= el
            else:
                for el in nums[:index]:
                    print(f'For left : {el}')
                    mult_left[index]*= el

                for el in nums[index+1:]:
                    print(f'For right : {el}')
                    mult_right[index]*= el
            
            output[index] = mult_left[index]*mult_right[index]
        
        return output

            