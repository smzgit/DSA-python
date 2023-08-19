from collections import deque
from pprint import pprint


class Graph:
    def __init__(self):
        self.__adj_list = dict()

    def add_vertex(self,v):
        if v not in self.__adj_list.keys():
            self.__adj_list[v] = []

    def add_edge(self,v1,v2):
        if v1 in self.__adj_list.keys() and v2 in self.__adj_list.keys():
            self.__adj_list[v1].append(v2)
            self.__adj_list[v2].append(v1)
            return True
        return False

    def bsf_shortest(self,start,end):
        if start==end:
            print(start)
            return start
        parent_dict=dict()
        visited=[start]
        que = deque([])
        que.append(start)
        parent_dict[start]=None

        while len(que):
            print(que)
            current_vertex=que.popleft()
            for v in self.__adj_list[current_vertex]:

                if v not in visited:
                    que.append(v)
                    visited.append(v)
                    parent_dict[v] = current_vertex

                    if v==end:
                        que.clear()
                        break
        print('parent =>',parent_dict)
        self.trace_path(parent_dict,start,end)

    def trace_path(self,parent_dict,start,end):
        path=[]
        current=end
        while parent_dict[current]:
            path.append(parent_dict[current])
            current=parent_dict[current]

        print(' -> '.join(path[::-1])+' -> ',end)


if __name__ == '__main__':
    my_graph = Graph()
    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')
    my_graph.add_vertex('E')
    #edges
    my_graph.add_edge('A',"B")
    my_graph.add_edge('B',"C")
    my_graph.add_edge('B',"E")
    my_graph.add_edge('D',"E")
    my_graph.add_edge('C',"D")
    print('Graph =>')
    pprint(my_graph._Graph__adj_list)

    my_graph.bsf_shortest(start='A',end='C')
