class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = collections.defaultdict(int)

        for num in nums:
            ans[num] += 1

        # by calling ans.items() I get all key value pairs as a list of tuples
        output = ans.items()

        # now sorting the list of tuples, output:
        sorted_items = sorted(output, key = lambda x:x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
        