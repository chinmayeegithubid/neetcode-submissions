class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        post_index = 0

        for i in range(1, len(preorder)):
            while stack[-1].val == postorder[post_index]:
                stack.pop()
                post_index += 1

            node = TreeNode(preorder[i])
            parent = stack[-1]

            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

            stack.append(node)

        return root