"""

    이 장에서는 "최소 신장 트리(MST)"에 대한 개념과 이를 찾는 대표적인 알고리즈인 크루스칼 알고리즘과 프림 알고리즘을 다룹이다. MST는 연결된 가중치 그래프에서 가장 작은 가중치의 간선들을 선택해 모든 노드를 연결하는 트리입니다. 이는 여러 네트워크 최적화 문제에서 중요한 역할을 합니다. 

    * 최소 신장 트리 (MST)란? 
      - "신장 트리(Spanning Tree)"는 그래프 내의 모든 노드를 포함하면서 사이클이 없는 트리입니다. 
      - 최소 신장 트리는 신장 트리 중에서 간선의 가중치 합이 최소가 되는 트리를 의미합니다. 
      - 네트워크 연결, 도로 건설, 통신 네트워크 설계 등에서 최소 비용으로 연결하는 것이 목표일 때 MST 알고리즘을 사용합니다. 

    * MST를 구하는 알고리즘 
      1. 크루스칼 알고리즘(Kruskal's Algorithm): 간선을 가중치의 오름차순으로 정렬한 후, 사이클을 만들지 않는 한도 내에서 간선을 하나씩 선택하여 트리를 구성하는 방식입니다. 이때 유니온-파인드(Union-Find) 자료구조를 사용하여 사이클을 효율적으로 감지합니다. 
      2. 프림 알고리즘(Prim's Algorithm): 시작 노드에서 출발하여 연결된 간선 중에서 가장 작은 가중치를 선택하며 트리를 확장하는 방식입니다. "우선순위 큐(힙 자료구조)"를 사용해 가장 작은 가중치 간선을 효율적으로 선택합니다.    

"""

"""
   
    * 크루스칼 알고리즘 (Kruskal's Algorithm)
      크로스칼 알고리즘은 모든 간선을 가중치에 따라 정렬한 후, 가중치가 작은 간선부터 차례로 선택하여 신장 트리를 만듭니다. 사이클이 생기지 않도록 주의해야 하며, 유니온-파인드 알고리즘을 이용해 이를 방지합니다.
    * 절차:
      1. 간선들을 가중치에 따라 오름차순으로 정렬합니다. 
      2. 사이클을 만들지 않는 간선들을 순차적으로 선택해 나갑니다. 
      3. 선택한 간선들이 그래프 내 모든 노드를 연결하면 완료됩니다. 

"""
## 크루스칼 알고리즘 예제: 
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u: 
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else: 
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    mst = []
    disjoint_set = DisjointSet(n)
    edges.sort(key=lambda x: x[2]) # 간선을 가중치로 정렬

    for u, v , weight in edges: 
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

    return mst 

# 노드 개수 
n = 4
# 간선 목록 (노드1, 노드2, 가중치)
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]

# 최소 신장 트리 구하기 
mst = kruskal(n, edges)
print("MST:", mst) # MST: [(2, 3, 4),(0, 3, 5),(0, 1, 10)]



"""

    * 프림 알고리즘 (Prim's Algorithm)
      프림 알고리즘은 트리 구조를 점진적으로 확장하는 방식입니다. 시작점을 선택하고, 그 노드에서 가장 작은 가중치를 가진 간선을 선택해 트리를 확장해 나갑니다. 

    * 절차 : 
      1. 임의의 노드를 선택하여 시작합니다. 
      2. 해당 노드에 연결된 간선 중 가중치가 가장 작은 간선을 선택해 트리를 확장합니다. 
      3. 아직 연결되지 않은 노드 중에서 가장 작은 가중치의 간선을 선택하여 반복합니다. 

"""
## 프림 알고리즘 예제: 
import heapq 

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for next_to, next_weight in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_weight, to, next_to))
    return mst 

# 그래프 (노드: {연결노드: 가중치})
graph = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}   
}

# 최소 신장 트리 구하기 
mst = prim(graph,0)
print("MST:",mst) # MST: [(0,3,5),(3,2,4),(0,1,10)]



"""

    * 차이점 
      - 크루스칼 알고리즘은 간선을 기반으로 하고, 간선이 적은 희소 그래프에 적합합니다. 유지온-파인드를 통해 사이클을 감지합니다. 
      - 프림 알고리즘은 정점을 기반으로 하며, 노드와 간선이 모두 많은 경우에도 적합합니다. "우선순위 큐(힙)"를 통해 가중치가 가장 작은 간선을 효율적으로 선택합니다. 

    * 결론 
      Chapter 14에서는 최소 신장 트리(MST)의 개념과 이를 찾기 위한 크루스칼 및 프림 알고리즘을 다루었습니다. 이 알고리즘들은 네트워크 연결 문제에서 비용을 최소화하는 데 매우 유용하며, 그래프 이론에서 중요한 부분을 차지합니다.   

"""


