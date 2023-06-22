def solution(node, idx):
    def search_node(nd, i):
        if nd is None:
            return None
        while i:
            nd = nd.next_item
            i -= 1
        return nd

    if idx == 0:
        now_node = search_node(node, idx)
        pr = now_node.next_item
        now_node.next_item = None
        return pr

    previous_node = search_node(node, idx - 1)
    now_node = search_node(node, idx)
    previous_node.next_item = now_node.next_item
    return node
