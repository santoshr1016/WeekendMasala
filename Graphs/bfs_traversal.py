"""
Name : BFS Graph traversal
Author: Santosh
Date: Sept 23, 2018
Use of Queue DS
For DFS use stack
"""
from queue import Queue


class GraphNode(object):
    def __init__(self, name):
        self.name = name
        self.adj_list = []
        self.visited = False
        self.predecessor = None


class Traversal(object):

    def bfs(self, start_node):
        queue = Queue()
        queue.put(start_node)
        start_node.visited = True

        while not queue.empty():
            actual_node = queue.get()
            print(actual_node.name)
            for vertex in actual_node.adj_list:
                if not vertex.visited:
                    vertex.visited = True
                    queue.put(vertex)

    def dfs(self, start_node):
        start_node.visited = True
        print(start_node.name)

        for vertex in start_node.adj_list:
            if not vertex.visited:
                self.dfs(vertex)


node_A = GraphNode("A")
node_B = GraphNode("B")
node_C = GraphNode("C")
node_D = GraphNode("D")
node_E = GraphNode("E")

node_A.adj_list.append(node_B)
node_A.adj_list.append(node_C)
node_B.adj_list.append(node_D)
node_D.adj_list.append(node_E)

traversal = Traversal()

traversal.bfs(node_A)

print("*"*22)


node_A = GraphNode("A")
node_B = GraphNode("B")
node_C = GraphNode("C")
node_D = GraphNode("D")
node_E = GraphNode("E")

node_A.adj_list.append(node_B)
node_A.adj_list.append(node_C)
node_B.adj_list.append(node_D)
node_D.adj_list.append(node_E)
traversal = Traversal()
traversal.dfs(node_A)
