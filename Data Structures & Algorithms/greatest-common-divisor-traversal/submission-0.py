class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False

        maximum = max(nums)
        spf = list(range(maximum + 1))

        # Build the smallest-prime-factor table.
        for prime in range(2, int(maximum ** 0.5) + 1):
            if spf[prime] == prime:
                for multiple in range(prime * prime, maximum + 1, prime):
                    if spf[multiple] == multiple:
                        spf[multiple] = prime

        parent = list(range(n))
        size = [1] * n
        components = n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a: int, b: int) -> None:
            nonlocal components
            a, b = find(a), find(b)

            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]
            components -= 1

        owner = {}

        for i, value in enumerate(nums):
            while value > 1:
                prime = spf[value]

                if prime in owner:
                    union(i, owner[prime])
                else:
                    owner[prime] = i

                while value % prime == 0:
                    value //= prime

        return components == 1