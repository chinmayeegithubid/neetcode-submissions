from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        size = [1] * len(accounts)

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        email_owner = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_owner:
                    union(i, email_owner[email])
                else:
                    email_owner[email] = i

        groups = defaultdict(list)

        for email, owner in email_owner.items():
            groups[find(owner)].append(email)

        return [
            [accounts[root][0]] + sorted(emails)
            for root, emails in groups.items()
        ]