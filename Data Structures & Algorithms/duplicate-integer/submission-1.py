class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # dicty = {}
        # for num in nums:
        #     dicty[num] = dicty.get(num, 0) + 1
        #     if dicty[num] > 1:
        #         return True
        # return False
        
     