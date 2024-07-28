
"""
    - 시간 복잡도 (Time Complexity)
        - 시간 복잡도는 알고리즘의 성능을 나타내는 지표 중 하나로, 입력 크기 n에 대한 함수로 표현됩니다. 이는 주어진 입력 크기 n에 대해 알고리즘이 얼마나 많은 연산(기본 연산)이 단계를 수행하는지를 측정합니다. 
"""

"""
    - 주요 시간 복잡도 종류 :
        1. 상수 시간 (Constant Time) - O(1):
            - 입력 크기와 상관없이 항상 일정한 시간 안에 알고리즘이 완료됩니다. 
            - 예 : 배열의 특정 인덱스에 접근하는 경우. 
        2. 로그 시간 (Logarithmic Time) - O(log n):
            - 입력 크기가 커질수록 실행 시간이 로그 함수에 비례하여 증가합니다.
            - 예 : 이진 탐색 알고르짐. 
        3. 선형 시간 (Linear Time) - O(n):
            - 입력 크기에 비례하여 실행 시간이 증가합니다. 
            - 예 : 배열에서 특정 값을 찾는 경우. 
        4. 선형 로그 시간 (Linearithmic Time) - O(n log n):
            - 입력 크기가 커질수록 실행 시간이 n과 log n 의 곱에 비례하여 증가합니다. 
            - 예 : 병합 정렬, 퀵 정렬 (평균적)
        5. 제곱 시간 (Quadratic Time) - O(n^2):
            - 입력 크기가 커질수록 실행 시간이 입력 크기의 제곱에 비례하여 증가합니다. 
            - 예 : 버블 정렬, 삽입 정렬 (최악의 경우)
        6. 지수 시간 (Exponential Time) - O(2^n):
            - 입력 크기가 커질수록 실행 시간이 지수 함수에 비례하여 급격히 증가합니다. 
            - 예 : 피보나치 수열의 재귀적 계산 (비효율적 구현)
"""

## 예제

# 상수 시간 - O(1)
def constant_time_example(arr):
    return arr[0]

# 선형 시간 - O(n)
def linear_time_example(arr):
    for element in arr:
        print(element)

# 제곱 시간 - O(n^2)
def quadratic_time_example(matrix):
    for row in matrix:
        for element in row:
            print(element)


"""
    - 공간 복잡도 (Space Complexity)
        - 공간 복자도는 알고리즘이 실행되는 동안 필요한 메모리 공간의 양을 입력 크기 n에 대한 함수로 나타낸 것입니다. 이는 알고리즘이 사용하거나 할당하는 추가 메모리를 측정합니다. 
"""

"""
    - 주요 공간 복잡도 종류 : 
        1. 상수 공간 (Constant Space) - O(1):
            - 입력 크기와 상관없이 일정한 양의 메모리 공간만 필요합니다. 
            - 예 : 변수 하나만 사용하는 경우. 
        2. 로그 공간 (Logarithmic Space) - O(n): 
            - 입력 크기가 커질수록 필요한 메로리 공간이 로그 함수에 비례하여 증가합니다. 
            - 예 : 재귀 호출의 깊이가 log n 인 경우 
        3. 선형 공간 (Linear Space) - O(n):
            - 입력 크기에 비례하여 메모리 공간이 증가합니다. 
            - 예 : 배열에 입력 데이터를 저장하는 경우. 
        4. 제곱 공간 (Quadratic Space) - O(n^2): 
            - 입력 크기가 커질수록 필요한 메모리 공간이 입력 크기의 제곱에 비례하여 증가합니다. 
            - 예 : 2차원 행렬을 사용하는 경우.
"""

## 예제 

# 상수 공간 - O(1)
def constant_space_example(n):
    count = 0 
    for i in range(n):
        count += 1
    return count

# 선형 공간 - O(n)
def linear_space_example(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

# 제곱 공간 - O(n^2)
def quadratic_space_example(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i*j)
        matrix.append(row)
    return matrix


"""
    - 요약
        - 시간 복잡도는 알고리즘이 실행되는 동안 걸리는 시간을 나타내며, 입력 크기 n에 따른 성능을 분석합니다. 
        - 공간 복잡도는 알고리즘이 실행되는 동안 필요한 메모리 공간을 나타내며, 입력 크기 n에 따른 메모리 사용량을 분석합니다. 

    - 이 두 가지 개념은 알고리즘의 효율성을 평가하고 비교하는 데 중요한 역할을 합니다.
"""