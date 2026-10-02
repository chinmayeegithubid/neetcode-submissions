class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Insert each copy directly after its original node
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next

        # 2. Assign random pointers to copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # 3. Separate the lists and restore the original
        copy_head = head.next
        current = head

        while current:
            copy = current.next
            current.next = copy.next
            copy.next = copy.next.next if copy.next else None
            current = current.next

        return copy_head