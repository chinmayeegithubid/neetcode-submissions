class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.children:
                stack.extend(node.children)

        result.reverse()
        return result