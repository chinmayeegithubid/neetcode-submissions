class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = dict()
        for s in strs:
            temp = [0] * 26
            for i in s:
                temp [ ord(i) - 97 ] += 1
            temp = tuple(temp)
            if temp in data:
                data[temp].append(s)
            else:
                data[temp] = [s]
        return list(data.values())
        