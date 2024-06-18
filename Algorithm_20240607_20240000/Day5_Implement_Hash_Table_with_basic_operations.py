"""

    학습 목표 
        - 해시 테이블의 개념 이해 
        - 해싱 함수의 역할과 충돌 해결 방법 이해 
        - 파이썬으로 해시 테이블 구현 

    학습 내용 
        1. 해시 테이블의 개념
            - 해시 테이블은 key와 value를 저장하는 자료구조로, 빠른 검색, 삽입, 삭제가 가능하다. 
            - 해싱 함수는 키를 해시 값으로 변환하여 해시 테이블의 인덱스로 사용한다. 
            - 주요 개념 : 해시 함수(Hash Function), 해시 값(Hash Value), 충돌(Collision), 버킷(Bucket)
        2. 충돌 해결 방법 
            - 개방 주소법(Open Addressing): 충돌이 발생하면 다른 빈 버킷을 찾는다. 
            - 체이닝(Chaining): 충돌이 발생하면 링크드 리스트를 사용하여 같은 버킷에 여러 값을 저장한다. 
        3. 해시 테이블의 주요 연상 
            - 삽입(Insert)
            - 검색(Search)
            - 삭제(Delete)

"""

# 예제 코드 
# 1. 해시 테이블 클래스 구현 (체이닝을 사용한 충돌 해결)
class HashTable: 
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))

    def search(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                del bucket[i]
                return True
        return False 




