class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(11)
node2 = Node(22)
node3 = Node(33)
node4 = Node(44)
node5 = Node(55)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

root = node1

while root:
    print(root.data, end=" ")
    root = root.next

root = node1
left = None
right = None
while root:
    right = root.next
    root.next = left
    left = root
    root = right

print()

start = left
while start:
    print(start.data, end=" ")
    start = start.next