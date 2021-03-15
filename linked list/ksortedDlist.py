from .dlinkedlist import *
import heapq


def ksorted(head, k):
    if head is None:
        return head
    curr = head
    ptr = head
    i = 0
    heap = []
    heapq.heapify(heap)

    while curr is not None:
        if i == k + 1:
            ptr.data = heapq.heappop(heap)
            print(ptr.data, "ptr")
            ptr = ptr.next
        else:
            i += 1
        heapq.heappush(heap, curr.data)
        curr = curr.next

    while ptr is not None:
        ptr.data = heapq.heappop(heap)
        ptr = ptr.next
    return head


if __name__ == '__main__':

    p = DLinkedList()  # create a new linked list 'a'.
    nodes_p = [3, 6, 2, 12, 56, 8]
    k = 2
    for x in nodes_p:
        p.append(x)  # add to the end of the list
    printList(ksorted(p.head, k))
