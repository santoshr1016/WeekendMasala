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


def rev(node1):
    root = node1
    left = None
    right = None
    while root:
        right = root.next
        root.next = left
        left = root
        root = right
    return left


def get_length(l1):
    l = 0
    while l1:
        l += 1
        l1 = l1.next
    return l


def addTwoNumbers(l1, l2):
    l1 = rev(l1)
    l2 = rev(l2)
    carry = 0
    head = start = None
    while l1 and l2:
        sum = carry + l1.val + l2.val
        if sum >= 10:
            carry = 1
            sum = sum % 10
        else:
            carry = 0
        if not start:
            head = start = Node(sum)
        else:
            newnode = Node(sum)
            start.next = newnode
            start = start.next
        l1 = l1.next
        l2 = l2.next

    if l1:
        while l1:
            sum = carry + l1.val
            if sum >= 10:
                carry = 1
                sum = sum % 10
            else:
                carry = 0

            newnode = Node(sum)
            start.next = newnode
            start = start.next
            l1 = l1.next
    if l2:
        while l2:
            sum = carry + l2.val
            if sum >= 10:
                carry = 1
                sum = sum % 10
            else:
                carry = 0

            newnode = Node(sum)
            start.next = newnode
            start = start.next
            l2 = l2.next

    return rev(head)


h = addTwoNumbers(l1, l2)
while h:
    print(h.val, end="")
    h = h.next
