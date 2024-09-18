"""

    Chapter 13 : 최단 경로 알고리즘 

    Chap 13에서는 그래프 이론에서 중요한 개념 중 하나인 최단 경로 알고르짐에 대해 다룹니다. 이 알고리즘들은 그래프에서 두 노드 간의 가장 짧은 경로를 찾는데 사용됩니다. 다양한 문제 해결에 적용할 수 있으며, 대표적으로 네트워크 라우팅, 지리적 길찾기, 그리고 자원 배분 문제 등이 있습니다. 

    주요 개념 
    1. 가중 그래프(Weighted Graph): 각 간선(edge)에 가중치(weight)가 부여된 그래프입니다. 이 가중치는 두 노드 간의 거리, 비용, 시간 등을 나타낼 수 있습니다. 
    2. 단일 출발점 최단 경로(Single-Source Shortest Path): 그래프 내 특정 노드에서 다른 모든 노드로 가는 최단 경로를 찾는 문제입니다. 
    3. 모든 쌍 최단 경로(All-Pairs Shortest Path): 그래프의 모든 노드 쌍 간의 최단 경로를 찾는 문제입니다. 

    주요 알고리즘 
    1. 다익스트라 알고리즘 (Dijkstra's Algorithm)
        - 개요 : 단일 출발점 최단 경로 알고리즘 중 가장 많이 사용되는 방법입니다. 음의 가중치가 없는 그래프에서 출발 노드에서 다른 모든 노드로의 최단 경로를 찾습니다. 
        - 작동 방식 : 출발 노드를 기준으로 가장 가까운 노드부터 차례대로 차단 경로를 확정해 나가는 방식입니다. 
        - 시간 복잡도 : 일반적으로 O(V^2), 이진 힙을 사용하면 O((V + E) log V)로 최적화할 수 있습니다. 

    2. 벨만-포트 알고르즘 (Bellman-Ford Algorithm)
        - 개요 : 음의 가중치가 포함된 그래프에서 단일 출발점 최단 경로를 찾을 수 있는 알고리즘입니다. 다익스트라 알고리즘과 달리 음의 사이클이 존재하는 경우 이를 감지할 수 있습니다. 
        - 작동 방식 : 모든 간선을 최대 (V-1)번 반복하여 경로를 갱신하는 방식입니다. 
        - 시간 복잡도 : O(VE), 다익스트라보다 느리지만 음의 가중치가 있는 경우에도 동작합니다. 

    3. 플로이드-워셜 알고리즘 (Floyd-Warchall Algorithm)
        - 개요 : 모든 쌍 최단 경로 문제를 해결하는 알고리즘입니다. 그래프 내의 모든 노드 쌍에 대해 최단 경로를 계산합니다. 
        - 작동 방식 : 동적 계획법을 사용하여 그래프의 각 간선을 반복적으로 확인하고, 가능한 최단 경로를 갱신하는 방식입니다. 
        - 시간 복잡도 : O(V^3), 모든 쌍 간의 최단 경로를 계산하는데 사용됩니다. 

    예제 및 활용 
    - 네트워크 라이팅 : 인터넷에서 패킷을 보내는 최단 경로를 결정하는 데 사용됩니다. 
    - 지도 서비스 : Google Maps 같은 서비스에서 두 지점 간 최단 경로를 찾는데 사용됩니다. 
    - 공급망 최적화 : 자원의 운송 경로를 최적화하는 문제에 적용할 수 있습니다. 

"""

### 1. 다익스트라 알고리즘 (Dijkstra's Algorithm)
import heapq

def dijkstra(graph, start):
    # 최단 거리 저장하는 딕셔너리 
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0 

    # 우선순위 큐로 사용할 리스트 
    priority_queue = [(0, start)] # (거리, 노드)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        # 인접 노드 확인 
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 경로 발견 시 갱신 
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 그래프 예시 (딕셔너리로 표현)
graph = {
    'A': {'B': 1, 'C':4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 'A'에서 모든 노드까지의 최단 경로 찾기
print(dijkstra(graph,'A'))



### 2. 벨만-포드 알고리즘 (Bellman-Ford Algorithm)
def bellman_ford(graph, start):
    # 초기화 
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0 

    # V-1번 모든 간선을 확인하고 경로 갱신 
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
    
    # 음의 사이클 확인
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")
    
    return distance 

# 그래프 예시 (딕셔너리로 표현)
graph = {
    'A': {'B': 1, 'C':4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 'A'에서 모든 노드까지의 최단 경로 찾기 
print(bellman_ford(graph, 'A'))



### 3. 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
def floyd_warshall(graph):
    # 그래프 초기화 
    nodes = list(graph.keys())
    distance = {node: {node2: float('infinity') for node2 in nodes} for node in nodes}

    # 자기 자신으로 가는 거리는 0으로 설정 
    for node in nodes: 
        distance[node][node] = 0

    # 초기 그래프 거리 설정 
    for node in graph:
        for neighbor, weight in graph[node].items():
            distance[node][neighbor] = weight

    # 동적 계획법을 이용해 최단 경로 찾기 
    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance 

# 그래프 예시 (딕셔너리로 표현)
graph = {
    'A': {'B': 1, 'C':4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 모든 노드 간의 최단 경로 찾기 
result = floyd_warshall(graph)
for i in result:
    print(f"{i}: {result[i]}")



"""
    * 요약
        - 다익스트라 알고리즘 : 음의 가중치가 없는 그래프에서 단일 출발점 최단 경로를 찾음. 
        - 벨만-포드 알고르즘 : 음의 가중치가 있는 경우에도 단일 출발점 최단 경로를 찾음. 
        - 플로이드-워셜 알고르즘 : 모든 노드 쌍 간의 최단 경로를 찾음. 
"""  



