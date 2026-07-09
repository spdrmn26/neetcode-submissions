class Solution:
    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])           # read the length
            result.append(s[j+1 : j+1+length])  # read exactly 'length' chars
            i = j + 1 + length             # move pointer past this string
        return result