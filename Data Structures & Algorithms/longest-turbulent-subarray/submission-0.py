class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = longest = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up, down = down + 1, 1
            elif arr[i] < arr[i - 1]:
                up, down = 1, up + 1
            else:
                up = down = 1

            longest = max(longest, up, down)

        return longest