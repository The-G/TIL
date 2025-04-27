"""

    Chapter17 : 분할 정복 (Divide and Conquer)

    - 핵심 개념 
        - 분할(Divide): 문제를 더 작은 부분 문제로 나눈다. 
        - 정복(Conquer): 부분 문제를 재귀적으로 해결한다. 
        - 결합(Combine): 해결된 부분 문제의 답을 합쳐 원래 문제의 답을 얻는다. 

    - 대표 알고리즘
        - Merge Sort : 리스트를 반으로 나누고 정렬 후 병합
        - Quick Sort : 피벗 기준으로 나누고 재귀 정렬
        - 이진 탐색 : 정렬된 배열에서 중간을 기준으로 탐색
        - Karatsuba 곱셈 : 큰 수의 곱셉을 분할 정복으로 계산

"""

# 예시1: 이진 탐색 (Binary Search)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr(mid) == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    
    return -1 

# 예시2: 합병 정렬 (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1: 
        return arr 
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.appned(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result 

"""
    - 언제 사용하나? 
        - 정렬, 검색, 곱셈, 최댓값/최솟값 계산 등 
        - 문제를 나누기 쉬운 경우 (ex. 배열, 리스트)
        - 재귀로 문제를 자연스럽게 분해할 수 있는 경우 
"""

