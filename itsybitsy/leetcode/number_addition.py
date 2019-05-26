class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

node1 = Node(7)
node2 = Node(9)
node3 = Node(3)
node1.next = node2
node2.next = node3


l1 = node1

node1 = Node(2)
node2 = Node(6)
node3 = Node(9)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

l2 = node1


def add_two_numbers(l1, l2):
    curr = dummy = Node(0)
    p = l1
    q = l2
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        total = carry + x + y
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
        if p:
            p = p.next
        if q:
            q = q.next
    if carry > 0:
        curr.next = Node(carry)

    return dummy.next


h = add_two_numbers(l1, l2)
while h:
    print(h.val, end="")
    h = h.next
