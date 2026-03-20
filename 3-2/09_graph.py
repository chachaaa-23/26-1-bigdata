class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def show(self):
        for v, edges in self.graph.items():
            print(f"{v} -> {edges}")


g = Graph()
g.add_edge("Seoul", "Pohang")
g.add_edge("Pohang", "Busan")
g.add_edge("Seoul", "Suwon")
g.add_edge("Pohang", "Jeju")

g.show()
