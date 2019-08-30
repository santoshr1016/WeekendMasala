class Node(object):
    def __init__(self, name):
        self.name = name
        self.adj_list = []
        self.is_visited = False
        self.predecessor = None


class Graph(object):
    def bfs(self, start_node):
        queue = []
        queue.append(start_node)
        start_node.is_visited = True

        while queue:
            curr = queue.pop(0)
            print(curr.name)
            for node in curr.adj_list:
                if not node.is_visited:
                    node.is_visited = True
                    queue.append(node)

    def dfs(self, start_node):
        start_node.is_visited = True
        print(start_node.name)

        for curr in start_node.adj_list:
            if not curr.is_visited:
                self.dfs(curr)

    def dfs_iterative(self, start_node):
        stack = []
        start_node.is_visited = True
        stack.append(start_node)

        while stack:
            curr = stack.pop()
            print(curr.name)
            for node in curr.adj_list:
                if not node.is_visited:
                    node.is_visited = True
                    stack.append(node)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

nodeA.adj_list.append(nodeB)
nodeA.adj_list.append(nodeF)
nodeA.adj_list.append(nodeG)

nodeB.adj_list.append(nodeC)
nodeB.adj_list.append(nodeD)

nodeG.adj_list.append(nodeH)

nodeD.adj_list.append(nodeE)

graph = Graph()
graph.bfs(nodeA)
# print("*" * 22)
# graph.dfs(nodeA)
# graph.dfs_iterative(nodeA)

