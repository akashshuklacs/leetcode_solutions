class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        non_double_no = 0
        for num in nums:
            non_double_no ^= num
        return non_double_no
