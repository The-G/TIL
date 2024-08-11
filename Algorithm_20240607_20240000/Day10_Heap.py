"""
    chapter10은 "힙 (Heap)"에 대해 다루는 내용입니다. 힙은 특정 조건을 만족하는 이진 트리 기반의 자료구조로, 주로 우선순위 큐(Priority Queue)를 구현하는데 사용됩니다. 이 장에서는 최소 힙(min-heap)과 최대 힙(max-heap)을 포함하여 힙의 구조와 동작 원리, 그리고 힙을 사용하는 다양한 알고리즘을 설명합니다.
"""

"""
    # 주요 내용 
    1. 힙의 정의 및 특성 
        - 힙은 완전 이진 트리의 일종으로, 모든 노드가 자식 노드보다 크거나 같거나(최대 힙) 혹은 작거나 같은(최소 힙) 조건을 만족합니다. 
        - 힙은 배열로 표현될 수 있으며, 이를 통해 효율적인 저장 및 탐색이 가능합니다.
    2. 힙의 주요 연상 
        - 삽입(Insert): 새로운 원소를 힙에 추가하는 연산. 힙의 조건을 유지하기 위해 부모 노드와 비교하며 필요시 자리를 교환하는 방식으로 진행됩니다. 
        - 삭제(Delete): 주로 루트 노드를 삭제하고 마지막 노드를 루트에 위치시킨 후 힙의 조건을 유지하기 위해 자식 노드들과 교환하는 방식으로 진행됩니다. 
        - 힙 정렬(Heap Sort): 힙을 이용한 정렬 알고리즘으로, 주어진 리스트를 힙 구조로 만들고, 가장 큰(혹은 작은) 원소를 순서대로 추출하여 정렬합니다. 
    3. 힙의 구현 
        - 힙을 배열과 구현하는 방법과, 삽입 및 삭제 연상 시 시간 복잡도가 어떻게 되는지 설명합니다. 
        - 최대 힙과 최소 힙의 구현 방법을 다루고, 이들 간의 차이점과 사용 사례를 설명합니다. 
    4. 우선순위 큐
        - 힙을 이용한 우선순위 큐 구현에 대해 설명합니다. 우선순위 큐는 각 요소에 수선순위가 부여되어 있으며, 높은 우선순위를 가진 요소가 먼저 처리되는 큐입니다. 
        - 우선순위 큐의 다양한 응용 예제를 다룹니다. 
    5. 힙을 활용한 알고리즘
        - 힙 정렬(Heap Sort): 힙을 이용한 정렬 방법으로, 시간 복잡도는 'O(n log n) 입니다. 
        - 다익스트라 알고리즘: 최단 경로를 찾는 알고리즘에서 우선순위 큐(힙)를 사용하여 효율성을 높입니다. 
    
    이 장에서는 힙의 기본 개념부터 다양한 응용에 이르기가지 힙을 깊이 있게 탐구합니다. 특히, 힙을 기반으로 한 알고리즘들이 어떻게 구현되고 활용되는지 이해하는 것이 이 장의 핵심 목표입니다. 
"""


## 1. 최소힙(Min-Heap) 구현
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None 
    
    def peek(self):
        return self.heap[0] if self.heap else None 
    
    def size(self):
        return len(self.heap)
    
# # 예제 사용 
# min_heap = MinHeap()
# min_heap.insert(10)
# min_heap.insert(5)
# min_heap.insert(20)
# min_heap.insert(1)

# print("Min value:", min_heap.extract_min())
# print("Min value:", min_heap.extract_min())


# 2. 최대 힙(Max-Heap) 구현 
import heapq 

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, -val) # 음수를 넣어 최대 힙으로 만듦 

    def extract_max(self):
        return -heapq.heappop(self.heap) if self.heap else None 
    
    def peek(self):
        return -self.heap[0] if self.heap else None 
    
    def size(self):
        return len(self.heap)
    
# # 예제사용 
# max_heap = MaxHeap()
# max_heap.insert(10)
# max_heap.insert(5)
# max_heap.insert(20)
# max_heap.insert(1)

# print("Max value:", max_heap.extract_max())
# print("Max value:", max_heap.extract_max())


## 힙 정렬(Heap Sort) 구현 
def heap_sort(arr):
    min_heap = []
    sorted_arr = []

    # 모든 원소를 최소 힙에 삽입 
    for val in arr: 
        heapq.heappush(min_heap, val)

    # 힙에서 하나씩 꺼내 정렬된 배열에 추가 
    while min_heap:
        sorted_arr.append(heapq.heappop(min_heap))

    return sorted_arr 

# # 예제 사용 
# arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# sorted_arr = heap_sort(arr)
# print("Sorted array:", sorted_arr)


## 우선순위 큐(Priority Queue) 구현 
import heapq 

class PriorityQueue:
    def __init__(self):
        self.pq = [] 
        self.entry_finder = {}
        self.counter = 0 

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
        count = self.counter 
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
        self.counter += 1

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = '<removed-task>'

    def pop_task(self):
        while self.pq:
            priority, count , task = heapq.heappop(self.pq)
            if task != '<removed-task>':
                del self.entry_finder[task]
                return task 
        raise KeyError('pop from an empty priority queue')
    
# 예제 사용 
pq = PriorityQueue()
pq.add_task("task1", priority=5)
pq.add_task("task2", priority=1)
pq.add_task("task3", priority=3)
pq.add_task("task5", priority=4)
pq.add_task("task7", priority=2)

print("Next task:", pq.pop_task())
print("Next task:", pq.pop_task())

"""
    이 예제들은 힙의 기본 동작 원리를 이해하는 데 도움을 줄 것입니다. 
    힙을 이용해 min_value와 max_value를 효율적으로 관리하고, 우선순위 큐를 구현하는 방법을 익힐 수 있습니다.
"""