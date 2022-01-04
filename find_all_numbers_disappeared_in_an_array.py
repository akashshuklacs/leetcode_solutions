class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:        
        l = len(nums)
        set_of_vals_of_length_l = set([number for number in range(1, l+1)])
        existing_set = set(nums)
        return set_of_vals_of_length_l - existing_set
