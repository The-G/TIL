"""

    * 7일차: 그래프 (기본적인 개념)
    그래프는 다양한 문제를 해결하는 데 유용한 자료구조로, 특히 네트워크, 경로 찾기, 사회 연결망 분석 등에 사용됩니다. 7일차에는 그래프의 기본 개념을 배우고, 그래프를 구현하고 탐색하는 방법을 익힙니다. 

    학습 목표 
        - 그래프의 기본 개념 이해 
        - 그래프의 표현 방법 (인접 행렬, 인ㅂ 리스트)
        - 그래프 탐색 알고리즘 (DFS, BFS)

    * 7일차 학습 내용 

    1. 그래프의 기본 개념 
        - 그래프의 정의 : 정점(Node)과 간선(Edge)으로 구성된 자료구조. 
        - 그래프의 용어 :
            - 정점(Vertex): 그래프의 기본 단위 
            - 간선(Edge): 정점 간의 연결을 나타내는 선 
            - 무방향 그래프(Undirected Graph): 간선에 방향이 없는 그래프 
            - 유방향 그래프(Directed Graph): 간선에 방향이 있는 그래프 
            - 가중 그래프(Weighted Graph): 간선에 가중치가 있는 그래프 

    2. 그래프의 표현 방법 
        - 인접 행렬 (Adjacency Matrix): 2차원 배열로 그래프를 표현. 
        - 인접 리스트 (Adjacency List): 리스트의 리스트로 그래프를 표현. 

    3. 그래프 탐색 알고리즘 
        - 깊이 우선 탐색(DFS, Depth-First Search): 스택을 사오ㅛㅇ하거나 재귀적으로 구현. 
        - 너비 우선 탐색(BFS, Breadth-First Search): 큐를 사용하여 구현. 

"""

# 예제코드 

import networkx as nx 
import matplotlib.pyplot as plt

# Graph 클래스를 정의함. 
class Graph:
    def __init__(self):
        self.graph = {} # 그래프를 저장할 dictionary 생성 

    def add_vertex(self, vertex):
        # 정점을 그래프에 추가한다. 
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # 두 정점 간의 간선을 그래프에 추가한다. 무방향 그래프이므로 양쪽에 추가한다. 
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1) # 무방향 그래프의 경우 
    
    def dfs(self, start_vertex, visited=None):
        # 깊이 우선 탐색(DFS)을 수행한다. 
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        # 너비 우선 탐색(BFS)을 수행한다. 
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    
    def visualize(self):
        G = nx.Graph()
        for vertex in self.graph:
            G.add_node(vertex)
            for neighbor in self.graph[vertex]:
                G.add_edge(vertex, neighbor)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_color='black', edge_color='gray')
        plt.show()
    
# 예제 사용 
g = Graph()
vertices = ['A','B','C','D','E']
for vertex in vertices:
    g.add_vertex(vertex)

edges = [('A','B'),('A','C'),('B','D'),('C','E'),('A','E')]
for edge in edges:
    g.add_edge(edge[0], edge[1])

print("DFS: ")
g.dfs('A')

print("\n BFS: ")
g.bfs('A')

# 그래프 시각화 
g.visualize()


