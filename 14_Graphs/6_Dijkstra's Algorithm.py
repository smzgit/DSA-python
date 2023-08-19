import heapq

class Edge:
    def __init__(self, src, dest, wgt):
        self.source = src
        self.destination = dest
        self.weight = wgt

    def __str__(self):
        return f" {self.source.name} -> {self.destination.name} (wgt={self.weight}) "


class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.prev = None
        self.min_distance = float('inf')
        self.neighbours = []


    def __lt__(self, other):
        return self.min_distance < other.min_distance

    def add_edge(self,weight,dest):
        edge = Edge(src=self,wgt=weight,dest=dest)
        self.neighbours.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)

        while self.heap:
            current_vertex = heapq.heappop(self.heap)
            if current_vertex.visited:
                continue

            for edge in current_vertex.neighbours:
                print(str(edge))
                start = edge.source
                target = edge.destination
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.prev = start
                    heapq.heappush(self.heap,target)
            current_vertex.visited=True
    def shortest_path(self,vertex):
        print('Shortest Path to ',vertex.name)
        current_vertex = vertex
        path=[]
        while current_vertex is not None:
            path.append(current_vertex.name)
            current_vertex=current_vertex.prev
        print('Path :', ' -> '.join(path[::-1]))
if __name__ == '__main__':
    node_a = Vertex('A')
    node_b = Vertex('B')
    node_c = Vertex('C')
    node_d = Vertex('D')
    node_e = Vertex('E')
    node_f = Vertex('F')
    node_g = Vertex('G')
    node_h = Vertex('H')

    node_a.add_edge(6,node_b)
    node_a.add_edge(10,node_c)
    node_a.add_edge(9,node_d)

    node_b.add_edge(5,node_d)
    node_b.add_edge(16,node_e)
    node_b.add_edge(13,node_f)

    node_c.add_edge(6,node_d)
    node_c.add_edge(5,node_h)
    node_c.add_edge(21,node_g)

    node_d.add_edge(8,node_f)
    node_d.add_edge(7,node_h)

    node_e.add_edge(10,node_g)

    node_f.add_edge(4,node_e)
    node_f.add_edge(12,node_g)

    node_h.add_edge(2,node_f)
    node_h.add_edge(14,node_g)

    djikstra_algo = Dijkstra()
    djikstra_algo.calculate(node_a)
    djikstra_algo.shortest_path(node_e)
