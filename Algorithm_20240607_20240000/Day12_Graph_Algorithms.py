"""

    이 장에서는 그래프의 개념, 탐색 방법, 그리고 최단 경로 찾기와 같은 중요한 그래프 알고르짐을 공부합니다. 

    주요 내용: 
    1. 그래프의 기본 개념: 
        - 그래프는 정점(Vertex)과 간선(Edge)으로 구성된 자료 구조로, 다양한 관계를 모델링하는 데 사용됩니다. 
        - 그래프는 방향성 여부에 따라 방향 그래프(Directed Graph)와 무방향 그래프(Undirected Graph)로 나뉩니다. 
        - 간선이 가중치를 가질 경우 가중치 그래프(Weighted Graph)라고 부릅니다. 
    2. 그래프의 표현 방법: 
        - 인접 행렬(Adjacency Matrix): 정점들 사이의 연결 관계를 2차원 배열로 표현합니다. 
        - 인접 리스트(Adjaceney List): 각 정점의 이웃 정점들을 리스트로 표현합니다. 
    3. 그래프 탐색 알고리즘: 
        - 깊이 우선 탐색(DFS, Depth-First Search): 한 정점에서 출발하여 가능한 깊이까지 탐색한 후, 더 이상 갈 곳이 없으면 되돌아와 다른 경로를 탐색하는 방법입니다. 
        - 너비 우선 탐색(BFS: Breadth-First Search): 한 정점에서 출발하여 가까운 정점부터 차례로 탐색하는 방법입니다. 
    4. 최단 경로 알고르즘: 
        - 다익스트라 알고리즘(Dijkstra's Algorithm): 가중치가 있는 그래프에서 한 정점에서 다른 모든 정점가지 최단 경로를 찾는 알고르즘입니다. 가중치가 음수가 아닌 경우에만 사용됩니다. 
        - 벨만-포트 알고르즘(Bellman-Ford Algorithm): 음수 가중치가 있는 그래프에서도 사용할 수 있는 최단 경로 알고르즘입니다. 다익스트라 알고르짐보다 느리지만, 음수 사이클을 감지할 수 있습니다. 
    5. 최소 신장 트리(Minimum Spanning Tree, MST):
        - 크루스칼 알고리즘(Kruskal's Algorithm): 간선들을 가중치에 따라 정렬한 후, 가중치가 작은 것부터 선택하여 사이클을 만들지 않는 방식으로 최소 신장 트리를 구성합니다. 
        - 프림 알고르짐(Prim's Algorithm): 하나의 정점에서 시작하여 연결된 정점들 중 가장 작은 가중치를 가진 간선을 선택하며 최소 신장 트리를 구성합니다.  

"""

## 예제 코드: 타익스트라 알고르짐의 예제 코드를 살펴보겠습니다. 
import heapq 

def dijksta(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0 
    priority_queue = [(0,start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight 

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
            
    return distances

# 그래프 표현 
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# 'A'에서 다른 정점까지의 최단 경로
print(dijksta(graph, 'A'))
            

# 그래프 표현, 시각화     
import networkx as nx
import matplotlib.pyplot as plt

# NetworkX 그래프 생성
G = nx.Graph()

# 간선 추가
for vertex in graph:
    for neighbor, weight in graph[vertex]:
        G.add_edge(vertex, neighbor, weight=weight)

# 위치 설정 (spring_layout은 시각적으로 좋은 레이아웃을 제공)
pos = nx.spring_layout(G)

# 노드와 간선 시각화
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_color='black', edge_color='gray')

# 간선에 가중치 라벨 추가
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# 그래프 출력
plt.show()


"""

    이 코드에서는 다익스트라 알고르짐을 사용하여 그래프 내의 최단 경로를 계산합니다. 'heapq' 모듈을 사용하여 우선순위 큐를 구현함으로써 효율적으로 최단 경로를 찾습니다. 

"""
