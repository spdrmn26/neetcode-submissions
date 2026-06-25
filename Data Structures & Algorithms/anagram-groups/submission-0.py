class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The key in this problem is "Lexicographical Sorting"
        # If I sort all words lexicographically, then
        # all anagrams become the same word
        # so, what I can do is: Create a dict
        # iterate through "strs", sort each word lexicographically
        # check if that word exists in the dict already, if not
        # then append it as a key, and add the original word as a value

        # ------- Code -------#
        # Using a defaultdict means we don't have to manually create an empty list
        # the first time we see a new lexicographically sorted word.
        ans = collections.defaultdict(list)
        for word in strs:
            # 1. Sort the word and join it back into a string to make it hashable
            lex_word = "".join(sorted(word))

            # 2. Append the original word to the correct anagram bucket
            ans[lex_word].append(word)

        # 3. We just need to return the grouped lists, which are the dictionary's values
        return list(ans.values())
