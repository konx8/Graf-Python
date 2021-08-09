import sys
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1  # First node is always the root of
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)
g = Graph(10)
g.graph = [[0, 8, 7, 9, 0, 18, 0, 0, 0, 0],
           [8, 0, 7, 8, 0, 0, 0, 0, 5, 0],
           [7, 7, 0, 8, 7, 12, 10, 16, 0, 0],
           [9, 8, 8, 0, 18, 0, 0, 0, 9, 0],
           [0, 8, 7, 18, 0, 15, 9, 0, 15, 0],
           [18, 0, 12, 0, 15, 0, 6, 14, 0, 0],
           [0, 0, 10, 0, 9, 6, 0, 12, 14, 20],
           [0, 0, 16, 0, 0, 14, 12, 0, 5, 0],
           [0, 5, 0, 9, 15, 0, 14, 5, 0, 5],
           [0, 0, 0, 0, 0, 0, 20, 0, 5, 0]]
g.primMST()
