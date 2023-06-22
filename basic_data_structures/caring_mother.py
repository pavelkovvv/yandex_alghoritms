def solution(node, elem):
    index0 = 0
    while node:
        if elem == node.value:
            return index0
        node = node.next_item
        if node is None:
            return -1
        index0 += 1
