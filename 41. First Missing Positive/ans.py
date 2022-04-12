from ast import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        min_value = 1
        
        count = 0
        # for -ve number min is 1
        for num in range(len(nums)):
            if nums[count] > 0:
                break
            else:
                count = count + 1
        
        # if +ve start at 1 start increment min value by 1
        # else use min value 1 and return value
        if count < len(nums):
            if nums[count] == 1:
                min_value = nums[count] + 1
                count = count + 1
            else:
                return 1
                
        prev = nums[count -1]
        
        # if +ve nums start by 1 
        # and find the minimum +ve missing value
        for num in range(count, len(nums)):
            if nums[num] > prev + 1:
                min_value = prev + 1
                break
            else:
                min_value = nums[num] + 1
                prev = nums[num]
        return min_value
                
                