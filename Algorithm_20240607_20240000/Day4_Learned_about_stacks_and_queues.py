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

# 1. 스택(Stack)
class Stack:
    def __init__(self):
        self.items = [] # 슽택을 저장할 리스트를 초기화함. 

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            item = self.items[-1]  
            del self.items[-1]     
            return item            
    # def pop(self):
    #     if not self.is_empty():
    #         return self.items.pop()
    #     return None 
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None 
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# # 예제 사용 
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop()) # Output: 3 
# print(stack.peek()) # Output: 2
# print(stack.is_empty()) # Output: False
# print(stack.size()) # Output: 2


# 2. 큐(Queue)
class Queue:
    def __init__(self):
        self.items = [] 

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[-1]
        return None 
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
# 예제 사용 
queue = Queue() 
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) # 1
print(queue.front()) # 2 
print(queue.is_empty()) # False 
print(queue.size()) # 2 


# 실습 문제 풀이 예시 
# 1. 스택을 사용하여 문자열의 괄호 균형 확인 




        