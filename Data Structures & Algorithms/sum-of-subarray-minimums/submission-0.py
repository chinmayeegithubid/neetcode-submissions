class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        n = len(arr)

        for right in range(n + 1):
            while stack and (
                right == n or arr[stack[-1]] >= arr[right]
            ):
                index = stack.pop()
                left = stack[-1] if stack else -1

                count = (index - left) * (right - index)
                result = (result + arr[index] * count) % MOD

            if right < n:
                stack.append(right)

        return result