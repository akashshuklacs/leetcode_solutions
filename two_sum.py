class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_exists_at = dict()
        for i, num in enumerate(nums):
            if target -num  in val_exists_at:
                return i, val_exists_at[target-num]
            val_exists_at[num] = i