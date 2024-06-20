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
        # 해시 테이블을 초기화함. 주어진 크기(size)만큼의 빈 리스트를 만들었음. 
        self.size = size
        self.table = [[] for _ in range(size)]

    # 해시 함수를 정의, 주어진 키의 해시 값을 테이블 크기로 나눈 나머지를 반환한다. 
    def _hash_function(self, key):
        return hash(key) % self.size
        # if isinstance(key, str):
        #     hash_value = sum(ord(char) for char in key)
        # else:
        #     hash_value = int(key)
        # return hash_value % self.size
        # 해시함수 커스텀하게 정의할 수 있음. 다른 방법도 가능 
    
    def insert(self, key, value):
        # 주어진 key-value 쌍을 해시 테이블에 삽입한다. 
        hash_key = self._hash_function(key) # 키의 해시 값을 계산한다. 
        bucket = self.table[hash_key] # 해시 값을 인덱스로 사용하여 버킷을 찾는다. 
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key: # 버킷 내에서 동일한 키를 찾으면 값을 업데이트한다. 
                bucket[i] = (key, value)
                return 
        bucket.append((key, value)) # 동일한 키가 없으면 버킷에 새로운 key-value 쌍을 추가한다. 

    def search(self, key):
        # 주어진 키에 해당하는 값을 해시 테이블에서 검색한다. 
        hash_key = self._hash_function(key) # 키의 해시 값을 계산한다. 
        bucket = self.table[hash_key] # 해시 value를 인덱스로 사용하여 버킷을 찾는다. 
        for k, v in bucket:
            if k == key: # 버킷 내에서 동일한 key를 찾으면 해당 값을 반환한다. 
                return v
        return None # key를 찾지 못하면 None을 반환한다. 
    
    def delete(self, key):
        # 주어진 key에 해당하는 key-value 쌍을 해시 테이블에서 삭제한다. 
        hash_key = self._hash_function(key) # 키의 해시 값을 계산한다. 
        bucket = self.table[hash_key] # 해시 값을 인덱스로 사용하여 버킷을 찾는다. 
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key: # 버킷 내에서 동일한 키를 찾으면 해당 항목을 삭제한다. 
                del bucket[i]
                return True
        return False # 키를 찾지 못하면 False를 반환한다. 


## 예제 사용 
# 해시 테이블 생성 
ht =HashTable(10)

# 항목 삽입 
ht.insert("apple",10) 
ht.insert("banana",20) 
ht.insert("grape", 30)

# 항목 검색
print(ht.search("apple"))   # 10
print(ht.search("banana"))  # 20
print(ht.search("grape"))   # 30
print(ht.search("cherry"))  # None

# 항목 삭제 
ht.delete("banana")
print(ht.search("banana"))  # None

