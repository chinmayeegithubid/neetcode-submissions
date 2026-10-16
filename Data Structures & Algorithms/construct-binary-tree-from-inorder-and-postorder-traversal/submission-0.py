class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        stack = [root]
        index = len(inorder) - 1

        for i in range(len(postorder) - 2, -1, -1):
            new_node = TreeNode(postorder[i])
            node = stack[-1]

            if node.val != inorder[index]:
                node.right = new_node
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index -= 1

                node.left = new_node

            stack.append(new_node)

        return root