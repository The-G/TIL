
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

# Node 클래스는 연결 리스트의 각 노드를 정의함.
class Node:  
    def __init__(self,data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드를 가르키는 포인터 (초기에는 None으로 설정함)

# SinglyLinkedList 클래스는 단일 연결 리스트를 정의한다. 
class SinglyLinkedList: 
    def __init__(self):
        self.head = None # 연결 리스트의 첫 번째 노드를 가리키는 포인터 (초기에는 None으로 설정한다.)

    # aapend 메서드는 연결 리스트의 끝에 새 노드를 추가한다. 
    def append(self, data):
        new_node = Node(data) # 새로운 노드를 생성하여 데이터를 저장
        if not self.head: # 연결 리스트가 비어 있는 경우
            self.head = new_node # 새 노드를 첫 번째 노드로 설정한다. 
            return # 함수 종료 
        last_node = self.head # 리스트의 첫 번째 노드에서 시작 
        while last_node.next: # 마지막 노드를 찾기 위해 반복 돌림. 
            last_node = last_node.next # 다음 노드로 이동 
        last_node.next = new_node # 마지막 노드의 다음 포인터를 새 노드로 설정한다. 
    
    def print_list(self):
        current_node = self.head # 리스트의 첫 번째 노드에서 시작 
        while current_node: # 마지막 노드에 도달할 때까지 반복
            print(current_node.data, end="->") # 현재 노드의 데이터를 출력하고 '->'로 이어줌
            current_node = current_node.next # 다음 노드로 이동
        print(None) # 리스트의 끝을 표시하기 위해 출력 

# 예제 사용 
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list() # Output: 1->2->3->None

# 2. 연결 리스트의 종류 
# 이중 연결 리스트의 노드 클래스
class DNode:
    def __init__(self,data):
        # DNode는 Node와 다르게 prev에도 None으로 초기 값을 설정해 준다.    
        self.data = data  
        self.next = None 
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None # 이중 연결 리스트의 첫 번째 노드를 가리키는 포인터 (초기에는 None으로 설정한다.) 
    
    def append(self, data):
        new_node = DNode(data) # 붙여 넣는 값을 DNode로 생성하고 
        if not self.head: # 리스트에 처음 들어온 값이면, DNode를 첫 값으로 설정 
            self.head = new_node
            return 
        last_node = self.head # last_node를 기존 리스트의 첫번째 값으로 설정 
        while last_node.next: # 리스트의 마지막 노드를 찾기 위해서 반복 
            last_node = last_node.next # 다음 노드로 이동 (마지막 노드로 이동)
        last_node.next = new_node # 마지막 노드의 다음 포인터를 새 노드로 설정
        new_node.prev = last_node # 새 노드의 이전 포인터를 마지막 노드로 설정 

    def print_list(self):
        current_node = self.head
        while current_node: # 첫 노드에서 시작해서 반복해서 출력함. 
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print(None)

# 예제 사용 
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.print_list() # Output: 1 <-> 2 <-> 3 <-> None


# 실습 문제 풀이 예시 
# 1. 단일 연결 리스트에서 노드 삭제 
def delete_node(linked_list, key):
    current_node = linked_list.head # linked_list의 첫 값을 currenct_node로 지정 

    # currenct_node가 있고 해당 값이 key값과 같다면 currenct_node의 다음 값을 linked_list head 값으로 넣고, currenct_node는 지움.
    if current_node and current_node.data == key: 
        linked_list.head = current_node.next 
        current_node = None 
        return # 함수 종료

    # prev는 current_node의 이전 노드를 추적하기 위해 사용됨. 
    prev = None 
    # current_node가 존재하고, current_node의 데이터가 key와 일치하지 않는 동안 반복함.
    while current_node and current_node.data != key:
        prev = current_node # prev를 current_node로 설정하고 
        current_node = current_node.next # current_node를 다음 노드로 이동시킴 
    
    # 리스트를 끝까지 탐색했지만 key를 찾지 못한 경우임     
    if current_node is None:
        return # 그냥 함수 종료 
    
    # 찾은 노드를 삭제 
    prev.next = current_node.next
    current_node = None 

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
delete_node(sll,2)
sll.print_list() # Output: 1->3->None

# 이중 연결 리스트에서 요소 탐색 
def search_node(dll, key):
    current_node = dll.head # 리스트의 첫 번째 값부터 확인 
    while current_node: 
        if current_node.data == key: 
            return True # 찾았으면 True를 반환 
        current_node = current_node.next
    return False # 못 찾으면 False를 반환 

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print(search_node(dll, 2)) # Output: True
print(search_node(dll, 4)) # Output: False



