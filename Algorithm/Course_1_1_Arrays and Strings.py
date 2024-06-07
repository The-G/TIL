### 배열


## 1. 배열의 정의 및 특징 

# 배열의 정의 : 동일한 타입의 데이터를 연속된 메모리 공간에 저장하는 자료구조. 
# 파이썬에서는 리스트로 배열을 구현할 수 있음. 

# 배열 선언 
arr = [1,2,3,4,5]

# 배열의 길이 
print(len(arr)) # Output: 5

# 배열 요소 접근 
print(arr[1]) # Output: 2

# 배열 요소 삽입 
arr.append(6) # 배열의 끝에 요소 추가 
print(arr) # Output: [1,2,3,4,5,6]

# 배열의 요소 삭제 
arr.remove(3) # 값이 3인 요소 삭제 
print(arr) # Output: [1,2,4,5,6]


## 2. 문자열 (String)
# 문자열 정의: 문자들의 연속된 시퀀스 
# 파이썬에서 문자열은 불변(immutable) 객체 

# 문자열 선언 
s = "hello"

# 문자열 길이 
print(len(s)) # Output: 5

# 문자열 접근 
print(s[0]) # Output: 'h'

# 무자열 슬라이싱 
print(s[1:4]) # Output: 'ell'

# 문자열 합치기 
s2 = "world" 
s3 = s + " " + s2
print(s3) # Output: 'hello world'

# 문자열 검색 
print(s.find("e")) # Output: 1 


## 실습 문제 풀이 
# 1. 배열에서 특정 요소 찾기 
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return - 1 # 요소가 없으면 -1 반환 

arr = [1,2,3,4,5]
target = 3
print(find_element(arr, target)) # Output: 2 

# 회문인지 확인하는 함수 
def is_palindrome(s):
    return s == s[::-1]

s = "racecar"
print(is_palindrome(s)) # Output: True

s = "hello"
print(is_palindrome(s)) # Output: False

