class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.sentinel = None

    def create_tree(self, value=0):
        self.sentinel = Node(value)

    def get_root(self):
        return self.sentinel.left

    def add_node(self):
        root = self.get_root()
        if not root:
            val = int(input("Enter Root Node Data:"))
            self.sentinel.left = Node(val)
        else:
            while True:
                inp = int(input("Enter 0 for left and 1 for right for Node {0}: ".format(root.data)))
                if inp:
                    if root and root.right:
                        root = root.right
                    else:
                        val = int(input("Enter data:"))
                        root.right = Node(val)
                        print("Node Added to right")
                        break
                else:
                    if root and root.left:
                        root = root.left
                    else:
                        val = int(input("Enter data:"))
                        root.left = Node(val)
                        print("Node Added to left")
                        break

    def inorder(self, root):
        if not root:
            return
        else:
            if root.left:
                self.inorder(root.left)
            print(root.data)
            if root.right:
                self.inorder(root.right)

t = Tree()
t.create_tree()
for i in range(5):
    t.add_node()
t.inorder(t.get_root())

