class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force is O(n^2)
        # O(n) approach needs storing into dictionary
        # Since I need to return the index, not the value
        # if I simply sort then I lose the index value
        # of course sorting makes this O(nLogn)
        new = sorted(nums)
        i, j = 0, len(nums) - 1
        m, n = 0, 0
        while i < j:
            if new[i] + new[j] < target:
                i+= 1
            elif new[i] + new[j] > target:
                j -= 1
            else: 
                m, n = new[i], new[j]
                break
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] == m or nums[i] == n:
        #         ans.append(i)
        # return ans
        idx1 = nums.index(m)
        if m == n:
            idx2 = nums.index(n, idx1 + 1)
        else:
            idx2 = nums.index(n)
        if idx2 < idx1: return [idx2, idx1]
        else: return [idx1, idx2]