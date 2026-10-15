class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        required_sum = k * threshold
        window_sum = 0
        count = 0

        for i, num in enumerate(arr):
            window_sum += num

            if i >= k:
                window_sum -= arr[i - k]

            if i >= k - 1 and window_sum >= required_sum:
                count += 1

        return count