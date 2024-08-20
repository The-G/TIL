"""

    1. 해시 맵 (Hash Map)
    해시 맵은 키-값 쌍(Key-Value Pair)으로 데이터를 저장하는 자료구조입니다. 키를 통해 데이터를 매우 빠르게 검색, 삽입, 삭제할 수 있습니다. 해시 맵은 내부적으로 해싱(Hashing)이라는 기법을 사용하는데, 해시 합수(Hash Function)를 통해 키를 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용해 배열에 데이터를 저장합니다. 
    
        - 해싱(Hashing) : 키를 입력으로 받아 고정된 크기의 해시 값을 반환하는 함수입니다.
        - 충돌(Collision) : 서로 (다른 키가 같은 해시 값을 반환하는 경우를 말합니다. 충돌을 처리하는 방법으로는 체이닝(Chaining)과 오픈 어드레싱(Open Addressing)이 있습니다. 

        장점 : 
            - 평균적으로 O(1)의 시간 복잡도로 데이터에 접근할 수 있습니다. 
            - 다양한 데이터 타입을 키로 사용할 수 있습니다.
        단점 :
            - 해시 함수가 비효율적일 경우 충돌이 많이 발생할 수 있습니다. 
            - 해시 맵의 메모리 사용량은 배열보다 클 수 있습니다. 

    2. 해시 셋 (Hash Set)
    해시 셋은 중복을 허용하지 않는 데이터 집합을 저장하는 자료구조입니다. 해시 셋은 내부적으로 해시 맵을 사용하여 구현되며, 각 요소가 고유한 해시 값을 가지도록 관리합니다. 해시 셋을 사용하면 특정 요소가 집합에 있는지 여부를 빠르게 확인할 수 있습니다.  

        특징 : 
            - 중복 요소를 호용하지 않습니다. 
            - 삽입, 삭제, 탐색이 평균적으로 O(1)의 시간 복잡도를 가집니다. 
            - 요소들의 순서는 보장되지 않습니다. 

"""

## 1. 해시 맵 예제 
class HashMap:
    def __init__(self, size=10):
        self.size = size 
        self.map = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        hash_key = self._hash(key)
        for kvp in self.map[hash_key]:
            if kvp[0] == key:
                kvp[1] = value 
                return 
        self.map[hash_key].append([key, value]) 
    
    def get(self, key):
        hash_key = self._hash(key)
        for kvp in self.map[hash_key]:
            if kvp[0] == key:
                return kvp[1]
        return None 
    
    def remove(self, key):
        hash_key = self._hash(key)
        for i, kvp in enumerate(self.map[hash_key]):
            if kvp[0] == key:
                del self.map[hash_key][i]
                return True
        return False

# 예제 사용 
hash_map = HashMap()
hash_map.put("apple", 1)
hash_map.put("banana", 2)
hash_map.put("orange", 3)

print(hash_map.get("apple"))
print(hash_map.get("banana"))

hash_map.remove("banana")
print(hash_map.get("banana"))


## 2. 해시 셋 예제 
class HashSet:
    def __init__(self):
        self.set = {}

    def add(self, value):
        self.set[value] = True 

    def contains(self, value):
        return value in self.set
    
    def remove(self, value):
        if value in self.set:
            del self.set[value]

# 예제 사용 
hash_set = HashSet()
hash_set.add(1)
hash_set.add(2)
hash_set.add(3)

print(hash_set.contains(2))
print(hash_set.contains(4))

hash_set.remove(2)
print(hash_set.contains(2))


"""

    체이닝과 오픈 어드레싱은 해시 충돌을 처리하는 두 가지 주요 방법입니다. 
    해시 충돌은 서로 다른 키들이 같은 해시 값을 가지게 될 때 발생합니다. 이 문제를 해결하기 위해 해시 테이블에서 체이닝과 오픈 어드레싱을 사용합니다. 

    1. 체이닝(Chaining)
    체이닝은 해시 충돌을 처리하는 가장 일반적인 방법 중 하나입니다. 각 해시 테이블 슬롯이 실제로는 **링크드 리스트(또는 다른 컬렉션 구조)**를 참조하도록 하는 방법입니다. 즉, 동일한 해시 값을 갖는 키들이 존재할 경우, 이 키들을 해당 슬롯에 연결 리스트로 저장하는 방식입니다. 
    
    - 작동 원리:
        - 해시 함수는 키를 해시 값으로 변환하여 해시 테이블의 인덱스를 계산합니다. 
        - 동일한 인덱스에 여러 개의 키-값 쌍이 존재할 수 있기 때문에, 이들을 링크드 리스트에 저장합니다. 
        - 검색 시, 해당 슬롯의 링크드 리스트를 순차적으로 탐색하여 원하는 키를 찾습니다. 
    - 장점:
        - 해시 테이블의 크기와 상관없이 충돌을 효과적으로 처리할 수 있습니다. 
        - 링크드 리스트는 동적으로 크기가 늘어나기 때문에, 저장 가능한 항목의 수가 제한되지 않습니다. 
    - 단점: 
        - 슬롯에 데이터가 많이 저장되면 링크드 리스트를 순차적으로 탐색해야 하기 때문에 성증이 저하될 수 있습니다.   
    
"""

## 예시 코드 (체이닝 사용):
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)] # 각 슬롯이 리스트(체이닝)를 가짐

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv 
            if k == key: 
                bucket[i] = (key, value) # 이미 존재하는 키는 값을 업데이트함
                return
        bucket.append((key, value)) # 새로운 키-값 쌍을 추가함

    def search(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None 


"""
    
    2. 오픈 어드레싱 (Open Addressing)
    오픈 어드레싱은 충돌이 발생했을 때, 다른 빈 슬롯을 찾아서 데이터를 저장하는 방식입니다. 링크드 리스트를 사용하지 않고 해시 테이블 자체의 다른 슬롯을 이용하여 충돌을 해결합니다. 

    오픈 어드레싱에는 여라 가지 방법이 있습니다. 
    - 선형 탐사 (Linear Probing): 충돌이 발생하면 다음 슬롯으로 이동하며 빈 슬롯을 찾습니다. 
    - 이차 탐사 (Quadratic Probing): 충돌이 발생하면, i^2 번째 슬롯으로 이동합니다. 
    - 이중 해싱 (Double Hashing): 두 개의 해시 함수를 사용하여 충돌 시 새로운 해시 값을 계산합니다. 

    - 장점: 
        - 추가적인 메모리 구조(예: 링크드 리스트)를 필요로 하지 않기 때문에, 메모리 효율이 높습니다. 
        - 해시 테이블 내의 데이터들이 연속된 메모리에 존재하므로, 캐시 효율이 좋습니다. 
    - 단점: 
        - 해시 테이블이 가득 차면, 충돌이 많이 발생하여 성능이 저하될 수 있습니다. 
        - 삭제 연산이 복잡해질 수 있습니다. 

"""

## 예시 코드 (선형 탐사 사용):
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size # 슬롯을 초기화 

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def _probe(self, hash_key):
        # 선형 탐사를 수행하여 다음 빈 슬롯을 찾음
        start = hash_key
        while self.table[hash_key] is not None:
            hash_key = (hash_key + 1) % self.size
            if hash_key == start:
                raise Exception("Hash table is full")
        return hash_key
    
    def insert(self, key, value):
        hash_key = self._hash_function(key)
        if self.table[hash_key] is None:
            self.table[hash_key] = (key, value)
        else:
            new_slot = self._probe(hash_key)
            self.table[new_slot] = (key, value)

    def search(self, key):
        hash_key = self._hash_function(key)
        start = hash_key
        while self.table[hash_key] is not None: 
            k, v = self.table[hash_key]
            if k == key:
                return v
            hash_key = (hash_key + 1) % self.size
            if hash_key == start:
                break
        return None 


"""

    체이닝과 오픈 어드레싱은 각각의 장단점이 있으며, 상황에 따라 적합한 방법을 선택해야 합니다. 체이닝은 메모리를 더 사용하지만 간단하고 충돌이 많을 때도 성능 저하가 덜한 반면, 오픈 어드레싱은 메모리 사용량이 적지만, 테이블이 가득 찼을 때 성능이 크게 저하될 수 있습니다. 

"""