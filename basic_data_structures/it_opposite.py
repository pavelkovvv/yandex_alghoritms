def solution(node):
    next_node = node
    i = 0
    while node:
        if i == 0:
            next_node = node.next
            node.prev = node.next
            node.next = None
            i += 1
        node = next_node
        if node.next is None:
            node.next = node.prev
            return node
        next_node = node.next
        node.next, node.prev = node.prev, node.next
