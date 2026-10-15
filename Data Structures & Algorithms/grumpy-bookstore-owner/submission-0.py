class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int],
                     minutes: int) -> int:
        baseline = 0
        extra = 0
        best_extra = 0

        for i, count in enumerate(customers):
            if grumpy[i] == 0:
                baseline += count
            else:
                extra += count

            if i >= minutes:
                extra -= customers[i - minutes] * grumpy[i - minutes]

            best_extra = max(best_extra, extra)

        return baseline + best_extra