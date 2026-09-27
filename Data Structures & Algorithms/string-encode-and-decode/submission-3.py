class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "_" + s
        return res

    def decode(self, s: str) -> List[str]:
        data = []
        index = 0
        while index < len(s):
            start = index
            while s[index] != '_':
                index += 1
            length = int(s[start:index])
            current = s[index+1 : index+1+length]
            data.append(current)
            index = index + 1 + length

        return data
