class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sum_nums = sum(nums)
        missing_num = int((n*(n-1)/2) - sum_nums)
        return missing_num