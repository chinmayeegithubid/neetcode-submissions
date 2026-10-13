from collections import defaultdict, Counter
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int],
                           website: List[str]) -> List[str]:
        visits = defaultdict(list)

        for time, user, site in sorted(zip(timestamp, username, website)):
            visits[user].append(site)

        scores = Counter()

        for sites in visits.values():
            scores.update(set(combinations(sites, 3)))

        best = min(scores, key=lambda pattern: (-scores[pattern], pattern))
        return list(best)