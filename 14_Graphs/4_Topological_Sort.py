from collections import deque as stk

class Graph:
    def __init__(self):
        self.__adj_list = dict()

    def add_vertex(self,v):
        if v not in self.__adj_list.keys():
            self.__adj_list[v] = []

    def add_edge(self,v1,v2):
        if v1 not in self.__adj_list.keys() and v2 not in self.__adj_list.keys():
            self.__adj_list[v1].append(v2)
            return True
        return False

    def top_sort(self,vertex,stack,visited):


        visited[vertex]=True
        for n in self.__adj_list[vertex]:
            if not visited[n]:
                self.top_sort(n,stack,visited)
        stack.append(vertex)




    def topological_sort(self,vertex_list):
        visited=dict()
        for v in vertex_list:
            visited[v] = False

        normal_stk = []
        for v in vertex_list:
            self.top_sort(v,normal_stk,visited)
        return normal_stk


if __name__ == '__main__':
    my_graph = Graph()


    v_list = [n for n in range(8)]
    print(v_list)
    for i in v_list:
        my_graph.add_vertex(i)
    my_graph.add_edge(7,5)
    my_graph.add_edge(7,6)
    my_graph.add_edge(6,4)
    my_graph.add_edge(6,3)
    my_graph.add_edge(5,2)
    my_graph.add_edge(5,4)
    my_graph.add_edge(2,1)
    my_graph.add_edge(3,1)
    my_graph.add_edge(1,0)
    ans=my_graph.topological_sort(v_list)
    print(ans[::-1])













