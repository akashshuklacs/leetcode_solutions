class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        curr_sum=nums[0]
        for num in nums[1:]:
            curr_sum=max(num, curr_sum+num) #start from current number or include current and prev numbers
            max_sum= max(curr_sum, max_sum)
        return max_sum