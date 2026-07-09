class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        return res

# Walkthrough
# encode(["leet", "co#de"])

#   "leet"  → len=4 → "4#leet"
#   "co#de" → len=5 → "5#co#de"
  
#   encoded = "4#leet5#co#de"

# decode("4#leet5#co#de")

#   i=0: find '#' at j=1, length=4, read s[2:6]="leet", i=6
#   i=6: find '#' at j=7, length=5, read s[8:13]="co#de", i=13
  
#   result = ["leet", "co#de"] ✅

# What length = int(s[i:j]) Reads
# It reads the digit characters before # and converts them to an integer.

# why not just length = int(s[j - 1])

# GitHub Copilot
# Because it only reads one digit — breaks for strings with 10+ characters

# s[i:j]  →  "5"    for length 5
# s[i:j]  →  "42"   for length 42
# s[i:j]  →  "100"  for length 100