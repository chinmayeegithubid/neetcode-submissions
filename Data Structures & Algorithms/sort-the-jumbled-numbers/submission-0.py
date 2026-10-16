class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(num):
            if num == 0:
                return mapping[0]

            value = 0
            place = 1

            while num:
                num, digit = divmod(num, 10)
                value += mapping[digit] * place
                place *= 10

            return value

        return sorted(nums, key=mapped_value)