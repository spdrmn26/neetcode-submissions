class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = collections.defaultdict(int)

        for num in nums:
            ans[num] += 1

        # O(N) complexity approach, using bucket sort
        # what if both 1 and 2 appear exactly twice? 
        # How do you put both of them into arr[2] if it 
        # only holds a single integer?
        arr = [[] for _ in range(len(nums) + 1)]

        for num, freq in ans.items():
            arr[freq].append(num)


        # now iterate arr from behind, and append 'k' numbers
        res = []
        for i in range(len(arr) - 1, 0, -1):
            # since there can be multiple numbers in arr[i]
            for num in arr[i]:
                res.append(num)
                # The moment we hit exactly K elements, we are done
                if len(res) == k:
                    return res
        return res
        