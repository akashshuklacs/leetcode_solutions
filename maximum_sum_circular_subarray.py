class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        max_sum=nums[0]
        min_sum=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max + num) 
            curr_min = min(num, curr_min + num)
            max_sum = max(curr_max, max_sum)
            min_sum = min(curr_min, min_sum)
        return max(max_sum, sum(nums) - min_sum)

#Explaination:
#If max is in non circular array, min must be in circular
#If min is in non circular array, max must be in circular
#Max of both must be max of circular array
#Except when all nos are negative, in that case go for max val in list