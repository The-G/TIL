
"""
    
    8일차 교육 : 고급 알고리즘 - 퀵 정렬 및 병합 정렬
    
    오늘의 교육 목표는 두 가지 고급 정렬 알고리즘인 퀵 정렬(Quick Sort)과 병합 정렬(Merge Sort)을 이해하고 구현하는 것이다. 이 두 알고리즘은 분할 정복 (Divide and Conquer) 기법을 사용하여 효율적인 정렬을 수행한다. 

"""


"""

    1. 퀵 정렬 (Quick Sort)
    퀵 정렬은 평균적으로 매우 빠른 정렬 알고리즘이다. 기본 아이디어는 피벗(pivot)을 선택하고, 피벗을 기준으로 배열을 두 개의 부분 배열로 분할한 후 각각을 정렬하는 것이다. 

    * 퀵 정렬의 단계 : 
        1. 피벗 선택 : 배열에서 하나의 요소를 피벗으로 선택
        2. 분할 : 피벗을 기준으로 작은 값들은 피벗의 왼쪽으로, 큰 값들은 피벗의 오른쪽으로 이동
        3. 재귀적 정렬 : 분할된 부분 배열을 재귀적으로 정렬한다. 

"""

# 퀵 정렬 구현 : 
def quick_sort(arr):
    # 배열의 길이가 1 이하인 경우, 배열을 반환한다. 
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr) // 2] # 피벗 요소를 배열의 중간 요소로 설정 
    left = [x for x in arr if x < pivot] # 피벗보다 작은 요소들은 left 리스트에 저장
    middle = [x for x in arr if x == pivot] # 피벗과 같은 요소들을 middle 리스트에 저장
    right = [x for x in arr if x > pivot] # 피벗보다 큰 요소들을 right 리스트에 저장

    # 재귀적으로 left와 right 리스트를 정렬하고, 이를 결합하여 정렬된 배열을 반환 
    return quick_sort(left) + middle + quick_sort(right) 

# 예제 수행 
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array : ", arr)
sorted_arr = quick_sort(arr)
print("Sorted array : ", sorted_arr)


"""

    2. 병합 정렬 (Merge Sort)
    병합 정렬은 안정적인 정렬 알고리즘으로, 항상 O(n log n)의 시간 복잡도를 가진다. 기본 아이디어는 배열을 반으로 나누고 각각을 정렬한 후 병합하는 것이다. 

    * 병합 정렬의 단계 : 
        1. 분할 : 배열을 두 개의 부분 배열로 나눈다. 
        2. 정렬 : 부분 배열을 재귀적으로 정렬한다. 
        3. 병합 : 정렬된 부분 배열을 병합하여 하나의 정렬된 배열로 만든다. 

"""

# 병합 정렬 구현 : 
def merge_sort(arr):
    # 배열의길이가 1 이하면 이미 정렬된 상태이므로 그대로 반환 
    if len(arr) <= 1:
        return arr
    
    # 배열을 두 개의 부분 배열로 분할한다. 
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 분할된 배열을 병합하여, 정렬된 배열을 반환한다. 
    return merge(left, right)

def merge(left, right):
    result = [] # 병합된 결과를 저장할 리스트를 초기화한다. 
    i = j = 0 # 왼쪽 배열(left)과 오른쪽 배열(right)의 인덱스를 초기화 

    # 두 배열의 요소를 비교하여 작은 값을 결과 리스트에 추가한다. 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 # 왼쪽 배열의 인덱스를 증가시킴 
        else:
            result.append(right[j])
            j += 1 # 오른쪽 배열의 인덱스를 증가시킴 
    
    # 남아있는 요소들을 결과 리스트에 추가한다. 
    result.extend(left[i:])  # 왼쪽 배열에 남아있는 요소들을 추가 
    result.extend(right[j:]) # 오른쪽 배열에 남아있는 요소들을 추가 

    return result

# 예제 수행 
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array : ", arr)
sorted_arr = merge_sort(arr)
print("Sorted array : ", sorted_arr)

"""

    * 과제 
        1. 퀵 정렬과 병합 정렬을 이해하고, 각각의 코드를 작성하여 테스트해 보세요. 
        2. 각 알고리즘의 시간 복잡도와 공간 복잡도를 분석해 보세요. 
        3. 두 알고리즘을 비교해보고, 어떤 경우에 어느 알고리즘이 더 유리한지 생각해 보세요.  

"""

"""

    2. 각 알고리즘의 시간 복잡도와 공간 복잡도를 분석해 보세요. 

    # 퀵 정렬 (Quick Sort)
        - 시간 복잡도 
            - 평균 시간 복잡도 : O(n log n)
                - 퀵 정렬은 평균적으로 O(n log n)의 시간 복잡도를 가집니다. 이는 배열을 두 개의 부분 배열로 분할하고, 각 부분 배열을 재귀적으로 정렬하는 과정에서 발생합니다. 
            - 최악 시간 복잡도 : O(n^2)
                - 피벗 선택이 항상 최악의 경우 (예: 가장 작은 또는 가장 큰 요소를 피벗으로 선택)가 발생하면, 퀵 정렬의 시간 복잡도는 O(n^2)가 됩니다. 이 경우 배열은 거의 정렬된 상태에서 퀵 정렬을 수행하게 되며, 이로 인해 효율이 떨어집니다. 
            - 최선 시간 복잡도 : O(n log n)
                - 피벗 선택이 항상 최적의 경우 (예: 배열의 중간 값)를 선택하면, 퀵 정렬의 시간 복잡도는 O(n log n)가 됩니다. 
        - 공간 복잡도 
            - 공간 복잡도 : O(log n)
                - 퀵 정렬은 제자리 정렬(in-place sorting) 알고리즘으로, 추가적인 메모리 공간을 거의 사용하지 않습니다. 다만, 재귀 호출에 의해 호출 스택이 사용되므로 공간 복잡도는 O(log n)가 됩니다. 최악의 경우에는 O(n)의 스택 공간이 필요할 수 있습니다. 

    # 병합 정렬 (Merge Sort)
        - 시간 복잡도
        
        - 공간 복잡도

        

"""