class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        first, second = p, q

        while first is not second:
            first = first.parent if first else q
            second = second.parent if second else p

        return first