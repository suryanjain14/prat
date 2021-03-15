from .linkedlist import *


def mid(head):
    prev = p2 = head
    while p2 is not None and p2.next is not None:
        prev = head
        head = head.next
        p2 = p2.next.next
        if p2 is None:
            return prev
        if p2.next is None:
            return head


def merge(lhead, rhead):
    prev = head = None
    if lhead is None:
        return rhead
    elif rhead is None:
        return lhead
    if lhead.data <= rhead.data:
        head = lhead
        lhead = lhead.next
        prev = head
    else:
        head = rhead
        rhead = rhead.next
        prev = head

    while lhead is not None and rhead is not None:
        if lhead.data <= rhead.data:
            prev.next = lhead
            prev = lhead
            lhead = lhead.next
        else:
            prev.next = rhead
            prev = rhead
            rhead = rhead.next
    if lhead is None:
        prev.next = rhead
    elif rhead is None:
        prev.next = lhead

    return head


def mergeSort(head):
    """
    :param head: head of unsorted linked list
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
    """
    if head is None:
        return head
    if head.next is None:
        return head

    md = mid(head)
    rhead = md.next
    md.next = None
    print(md.data, "mid")
    printList(head)

    left = mergeSort(head)
    right = mergeSort(rhead)
    return merge(left, right)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

# Node Class


if __name__ == '__main__':
    t = 1
    for cases in range(t):
        n = int(input())
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(mergeSort(p.head))
