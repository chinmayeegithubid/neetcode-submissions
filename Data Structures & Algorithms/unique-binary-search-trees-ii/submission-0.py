class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build(start, end):
            if start > end:
                return [None]

            trees = []

            for value in range(start, end + 1):
                left_trees = build(start, value - 1)
                right_trees = build(value + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(value)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)