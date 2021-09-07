class Graph:
    def __init__(self, num_nodes, nodes):
        self.num_nodes = num_nodes
        self.adj_mtx = [[0]*self.num_nodes for i in nodes]
        self.nodes = nodes

    def add_edge(self, node1, node2):
        indexOfNode1 = self.nodes.index(node1)
        indexOfNode2 = self.nodes.index(node2)

        self.adj_mtx[indexOfNode1][indexOfNode2] = 1
        self.adj_mtx[indexOfNode2][indexOfNode1] = 1
    
    def show_graph(self):
        for row in self.adj_mtx:
            print(row)

g = Graph(7, [0,1,2,3,4,5, 6])

g.add_edge(1, 5)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(0, 3)
g.add_edge(0, 6)
g.add_edge(4, 6)

g.show_graph()