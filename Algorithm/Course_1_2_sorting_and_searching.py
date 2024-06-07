
"""
    2일차: 기초 알고리즘
    학습 목표
        - 각각의 정렬 알고리즘과 탐색 알고리즘에 대한 이해
        - 각 알고리즘의 장단점과 시간 복잡도 분석
        - 파이썬으로 간단한 정렬 및 탐색 알고리즘 구현
    학습 내용
        1. 정렬 알고리즘 (Sorting Algorithms)
            - 버블 정렬 (Bubble Sort)
            - 선택 정렬 (Selection Sort)
            - 삽입 정렬 (Insertion Sort)
            - 퀵 정렬 (Quick Sort)
            - 합병 정렬 (Merge Sort)
        2. 탐색 알고리즘 (Searching Algorithms)
            - 선형 탐색 (Linear Search)
            - 이진 탐색 (Binary Search)
    실습 문제
        - 주어진 배열을 각각의 정렬 알고리즘을 사용하여 정렬하고 결과를 출력하는 함수 작성
        - 주어진 정렬된 배열에서 특정 요소를 각각의 탐색 알고리즘을 사용하여 찾고 인덱스를 반환하는 함수 작성

    학습 자료
        1. 정렬 알고리즘 (Sorting Algorithms)
            - 각 알고리즘의 개념, 동작 방식, 시간 복잡도에 대한 이해
            - 파이썬으로 각 알고리즘 구현 예제 참고
        2. 탐색 알고리즘 (Searching Algorithms)
            - 각 알고리즘의 개념, 동작 방식, 시간 복잡도에 대한 이해
            - 파이썬으로 각 알고리즘 구현 예제 참고

"""
# 실습 문제 풀이 
# 1. 정렬 알고르즘 구현 
def bubble_sort(arr):
    n = len(arr) # 배열의 길이를 n에 저장한다. 
    for i in range(n): # 배열 전체를 순회한다. 
        # 이미 정렬된 부분을 제외하고 배열의 나머지를 순회한다.    
        for j in range(0, n-i-1):  
            # 현재 요소가 다음 요소보다 크다면 두 요소를 교환한다. 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(i,"-",j,"단계 결과: ",arr)
            # 큰 수를 뒤로 미루는 방식으로 진행이 되네, 
            # 근데 중간에 교환이 필요 없어도 진행되는 부분이 불필요해 보이기도 함.. 

    return arr # 정렬된 배열을 반환한다. 

arr = [64,34,25,12,22,11,90]
print("최종결과"+" : ",bubble_sort(arr))

# 2. 탐색 알고리즘 구현 
def binary_search(arr, target): # 절반씩 나누며 tree처럼 값을 찾는 구조.
    # 초기화: low는 배열의 시작 인덱스 / high는 배열의 마지막 인덱스 
    low = 0 
    high = len(arr) - 1 # 0부터 시작이니 -1로 length 확인 

    # low가 high보다 작거나 같을 때까지 반복
    while low <= high:
        mid = (low + high) // 2 # 준간 인덱스 계산

        print("중간값은, ",arr[mid])

        # 중간 값이 목표 값과 같으면 인덱스 반환, 중간부터 찾네!! 
        if arr[mid] == target:
            return mid
        # 중간 값이 목표 값보다 작으면, 왼쪽 절반을 버리고 오른쪽 절반을 탐색
        elif arr[mid] < target:
            low = mid + 1 
        # 중간 값이 목표 값보다 크면, 오른쪽 절반을 버리고 왼쪽 절반을 탐색
        else:
            high = mid - 1 

    # 목표 값을 찾지 못하면 -1 반환 
    return -1

arr = [2,3,4,5,6,7,10,11,12,15,40]
target = 15

print("결과: ",binary_search(arr,target))
