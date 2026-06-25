class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Last solution used sorting, so it was O(N * KlogK) time complexity
        # There another way to solve it within O(N * K) time complexity

        ans = collections.defaultdict(list)

        # iterate
        for word in strs:

            # define an array for 26 length, initialized with all 0s
            count = [0] * 26
            
            for letter in word:
                # ord('') gets me the ascii value, (letter - a)
                # gets me numerical position of letter between 0 - 25
                count[ord(letter) - ord('a')] += 1

            # Cast the list to an immutable tuple so it can be a dict key
            ans[tuple(count)].append(word)

        return list(ans.values())
