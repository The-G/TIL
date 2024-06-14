"""

    4일차: 스택(Stack)과 큐(Queue)
    
    학습 목표
    - 스택과 큐의 기본 개념 이해
    - 스택과 큐의 주요 연산 이해
    - 파이썬으로 스택과 큐 구현
    - 스택과 큐의 활용 사례 이해
    
    학습 내용
    1. 스택(Stack)
        - 스택의 개념
        - LIFO(Last In, First Out) 구조
        - 주요 연산: push, pop, peek, is_empty
    2. 큐(Queue)
        - 큐의 개념
        - FIFO(First In, First Out) 구조
        - 주요 연산: enqueue, dequeue, front, is_empty
    
    실습 문제
    - 스택을 사용하여 문자열의 괄호 균형을 확인하는 함수 작성
    - 큐를 사용하여 주어진 수열의 순서를 뒤집는 함수 작성

"""

# 학습 자료 

# 1. 스택(Stack) / LIFO
class Stack:
    def __init__(self):
        self.items = [] # Stack을 저장할 리스트를 초기화한다. 

    def push(self, item):
        self.items.append(item) # 새 항목을 리스트의 끝에 추가한다. 

    # 리스트에서 element를 꺼내는 거임! 마지막 항목을 꺼냄. pop 
    def pop(self): 
        if self.is_empty(): # Stack이 비어있는 경우 None를 반환한다.
            return None
        else:
            item = self.items[-1] # 리스트의 마지막 항목을 item에 저장한다. 
            del self.items[-1] # 리스트에서 마지막 항목을 삭제한다.      
            return item # 저장했던 item을 반환한다.             

    # def pop(self):
    #     if not self.is_empty():
    #         return self.items.pop()
    #     return None 

    # 리스트의 마지막 항목을 확인만 하는 거임. peek 
    def peek(self):
        if not self.is_empty(): # 리스트가 비어있지 않다면, 
            return self.items[-1] # 리스트의 마지막 항목을 반환한다. 
        return None # 리스트가 비어있으면 None를 반환한다. 
    
    def is_empty(self):
        return len(self.items) == 0 # 리스트 길이가 0 이면 True가 반환된다. 
    
    def size(self):
        return len(self.items) # 리스트 길이를 반환한다. 

# # 예제 사용 
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop()) # Output: 3 
# print(stack.peek()) # Output: 2
# print(stack.is_empty()) # Output: False
# print(stack.size()) # Output: 2


# 2. 큐(Queue) / FIFO
class Queue:
    def __init__(self):
        self.items = [] # Queue를 저장할 리스트를 초기화한다. 

    # enqueue 메서드는 큐의 뒤에 항목을 추가한다. 
    def enqueue(self, item):
        self.items.insert(0, item) # 새 항목을 리스트의 맨 앞에 삽입하여 큐의 뒤에 추가한다.         
        # 큐의 앞(front)은 리스트의 끝쪽에 있고, 큐의 뒤(rear)는 리스트의 시작쪽에 있다고 생각하면 혼동이 없다!!         

    # dequeue 메서드는 큐의 앞에 있는 항목을 제거하고 반환한다. 
    def dequeue(self):
        if not self.is_empty(): # 큐가 비어 있지 않으면, 
            return self.items.pop() # 리스트의 마지막 항목을 제거하고 반환한다. 
        return None
    
    # front 메서드는 큐의 앞에 있는 항목을 반환한다. 
    def front(self):
        # 큐가 비어있지 않으면, 리스트의 마지막 항목을 반환한다. 비어있으면 None를 반환한다. 
        if not self.is_empty():
            return self.items[-1]  
        return None 
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
# # 예제 사용 
# queue = Queue() 
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue.front()) # 1 
# print(queue.dequeue()) # 1
# print(queue.front()) # 2
# queue.enqueue(4)
# print(queue.is_empty()) # False 
# print(queue.size()) # 3
# print(queue.front()) # 2

