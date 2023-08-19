from pprint import pprint


class Graph:
    def __init__(self, gd=None):
        if not gd:
            self.gd = gd
        self.gd = dict()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.gd.keys() and vertex2 in self.gd.keys():
            self.gd[vertex1].add(vertex2)
            self.gd[vertex2].add(vertex1)
            return True
        return False

    def add_vertex(self, vertex):
        if vertex not in self.gd.keys():
            self.gd[vertex] = set()
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.gd.keys():
            for v in self.gd[vertex]:
                self.gd[v].remove(vertex)
            del self.gd[vertex]
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.gd.keys() and v2 in self.gd.keys():
            self.gd[v1].remove(v2)
            self.gd[v2].remove(v1)
            return True
        return False


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', "B")
    graph.add_edge('A', "C")
    graph.add_edge('A', "D")
    graph.add_edge('B', "E")
    graph.add_edge('D', "E")
    graph.add_edge('D', "C")

    pprint(graph.gd)
    # print('After removing E')
    # graph.remove_vertex('E')
    # pprint(graph.gd)

    print('After removing edge between A & D')
    graph.remove_edge('A', "D")
    pprint(graph.gd)
