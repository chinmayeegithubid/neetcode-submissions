from functools import cache


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []

        @cache
        def build(size):
            if size == 1:
                return [TreeNode(0)]

            trees = []

            for left_size in range(1, size - 1, 2):
                right_size = size - 1 - left_size

                for left in build(left_size):
                    for right in build(right_size):
                        trees.append(TreeNode(0, left, right))

            return trees

        return build(n)