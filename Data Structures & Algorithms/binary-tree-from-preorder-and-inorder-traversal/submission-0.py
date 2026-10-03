class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for i in range(1, len(preorder)):
            node = stack[-1]
            child = TreeNode(preorder[i])

            if node.val != inorder[inorder_index]:
                node.left = child
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1

                node.right = child

            stack.append(child)

        return root