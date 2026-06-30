class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer problem
        # since here a palindrome can be a sentence as well
        # with first letter as capital and last as small
        # eg: Input: s = "Was it a car or a cat I saw?"
        # Output: true
        # (ord(s[i]) - ord(s[j]) == 32)): 32 is the difference
        # between Capital and Small ASCII alphabets
        i, j = 0, len(s) - 1
        while i < j:
            # skip if alpha-numeric:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True