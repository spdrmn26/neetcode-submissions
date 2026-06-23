class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Since this asks for an anagram - storing in a set
        # will not work, I need characters and count
        # both to match, so I need to store in a dict
        # resulting dict should be same
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for c, d in zip(s, t):
            s_dict[c] = s_dict.get(c, 0) + 1
            t_dict[d] = t_dict.get(d, 0) + 1
        return s_dict == t_dict
