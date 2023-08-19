from pprint import pprint
from collections import deque as dq


class Graph:
    def __init__(self):
        self.__gd = dict()

    def add_vertex(self, v):
        if v not in self.__gd.keys():
            self.__gd[v] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.__gd.keys() and v2 in self.__gd.keys():
            self.__gd[v1].append(v2)
            self.__gd[v2].append(v1)
            return True
        return False

    def DFS_traversal(self, start_vertex=0):
        print('\nDFS Traversal =>')
        stk = dq([])
        visited = [start_vertex]
        stk.append(start_vertex)
        while len(stk) > 0:
            print('Stk =>', stk)
            print('visited =>', visited)
            ele = stk.pop()
            print('current_pos = ', ele)

            print('------------------------------------')
            for eles in self.__gd[ele]:
                if eles not in visited:
                    visited.append(eles)
                    stk.append(eles)


if __name__ == '__main__':
    print('Graph Adjacency List =>')
    # Refer dummy_graph.png to visualize the graph
    # BFS of dummy_graph.png :0 1 3 2 5 6 4
    gp = Graph()
    gp.add_vertex(0)
    gp.add_vertex(1)
    gp.add_vertex(2)
    gp.add_vertex(3)
    gp.add_vertex(4)
    gp.add_vertex(5)
    gp.add_vertex(6)
    # edges
    gp.add_edge(0, 1)
    gp.add_edge(0, 3)
    gp.add_edge(1, 3)
    gp.add_edge(1, 2)
    gp.add_edge(1, 6)
    gp.add_edge(1, 5)
    gp.add_edge(2, 5)
    gp.add_edge(3, 2)
    gp.add_edge(3, 4)
    gp.add_edge(4, 2)
    gp.add_edge(4, 6)
    pprint(gp._Graph__gd)
    gp.DFS_traversal()
