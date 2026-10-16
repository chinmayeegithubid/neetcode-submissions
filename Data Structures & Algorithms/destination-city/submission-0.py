class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = {start for start, end in paths}

        for start, end in paths:
            if end not in outgoing:
                return end