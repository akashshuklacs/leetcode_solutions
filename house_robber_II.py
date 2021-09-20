class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        robbed_till_now1=0#if starting from first house
        robbed_till_now2=0#if starting from second house
        a=0 #previous to previous house
        b=0 #previouse house
        for i in range(0, len(nums)-1): #i is current house
            robbed_till_now1 = max(a+nums[i], b) #max of: prev house if you skip current
                                                 # or rob current house
            a=b
            b=robbed_till_now1
        a=0
        b=0
        for i in range(1, len(nums)):
            robbed_till_now2 = max(a+nums[i], b)
            a=b
            b=robbed_till_now2
        return max(robbed_till_now1, robbed_till_now2)