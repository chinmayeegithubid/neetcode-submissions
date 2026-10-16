class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        if k > 0:
            left, right = 1, k
        else:
            left, right = n + k, n - 1

        window_sum = sum(code[i] for i in range(left, right + 1))

        for i in range(n):
            result[i] = window_sum
            window_sum -= code[left % n]
            left += 1
            right += 1
            window_sum += code[right % n]

        return result