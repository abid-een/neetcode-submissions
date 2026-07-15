class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_without_duplicate = set(nums)
        if len(nums_without_duplicate)!=len(nums):
            return True
        else:
            return False