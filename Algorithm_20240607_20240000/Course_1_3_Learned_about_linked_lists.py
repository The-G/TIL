
"""

    3일차: 연결 리스트 (Linked List)
    
    학습 목표
        - 연결 리스트의 기본 개념 이해
        - 연결 리스트의 종류와 각각의 특징
        - 파이썬으로 연결 리스트 구현
        - 연결 리스트를 사용한 기본 연산 (삽입, 삭제, 탐색)
    학습 내용
        1. 연결 리스트의 개념
            - 정의 및 구조
            - 연결 리스트와 배열의 비교
        2. 연결 리스트의 종류
            - 단일 연결 리스트 (Singly Linked List)
            - 이중 연결 리스트 (Doubly Linked List)
            - 원형 연결 리스트 (Circular Linked List)
        3. 연결 리스트의 기본 연산
            - 노드 삽입
            - 노드 삭제
            - 노드 탐색
    
    실습 문제
        - 단일 연결 리스트에서 주어진 값의 노드를 찾아서 삭제하는 함수 작성
        - 이중 연결 리스트를 구현하고, 앞에서부터 요소를 탐색하는 함수 작성

"""

## 학습 자료 
# 1. 연결 리스트의 개념 
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class SinglyLinkedList: 
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
            return 
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node 
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(None)

# 예제 사용 
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list() # Output: 1->2->3->None

# 2. 연결 리스트의 종류 
