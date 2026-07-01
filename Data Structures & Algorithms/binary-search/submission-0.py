class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        s_i, e_i = 0, l - 1 # start index and end index
        while s_i <= e_i:
            k = e_i + s_i // 2 # built-in integer division operator // which divides & floors
            if nums[k] == target:
                return k
            elif nums[k] > target:
                s_i = 0
                e_i = k - 1
            elif nums[k] < target:
                s_i = k + 1
                e_i = e_i
        return -1
