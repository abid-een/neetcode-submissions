class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_nums = set()
        for i in nums:
            if i in has_nums:
                return True
            else:
                has_nums.add(i)
        return False