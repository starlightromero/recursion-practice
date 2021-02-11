def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    node = None
    if l1.val < l2.val:
        node = l1
        node.next = mergeTwoLists(l1.next, l2)
    else:
        node = l2
        node.next = mergeTwoLists(l1, l2.next)
    return node
