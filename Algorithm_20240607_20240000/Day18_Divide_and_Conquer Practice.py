"""

    Chapter18 : 대표 문제 풀이 (분할 정복)

    - 중요 목표 
        - 분할 정복을 활용한 문제 해결 전략 익히기 
        - 실전에서 자주 등장하는 문제들을 직접 풀어보기 

    - 대표 문제 1 : 이진 검색 트리(BST) 만들기 
        - 문제 설명, 정렬된 배열이 주어졌을 때, 군형 잡힌 이진 검색 트리(BST)를 만들어보자. 

"""

# 입력 예시 
nums = [-10, -3, 0 , 5, 9]
# 출력 구조 (BST)
# 중간값을 루트로 잡아 좌우로 분할해 재귀적으로 트리를 만듦. 

"""
    - 해결 전략
        - 배열의 중앙 값을 루트로 설정. 
        - 왼쪽 절반은 왼쪽 서브트리로, 오른쪽 절반은 오른쪽 서브트리로 설정.
        - 재귀적으로 반복. 
"""

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

def sorted_array_to_bst(nums):
    if not nums: 
        return None 
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])

    return root 

def print_tree(node, level=0, prefix="Root:"):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")

# 테스트 
nums = [-10, -3, 0, 5, 9]
bst_root = sorted_array_to_bst(nums)
print_tree(bst_root)

"""
    - 대표 문제 2: 합병 정렬 (Merge Sort)
        - 이건 분할 정복 알고리즘의 대표 중 대표임. 
    - 문제 설명, 배열을 오름차순으로 정렬하되, Merge Sort를 이용하여 정렬하라. 
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0 

    # 두 배열을 병합 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result 

# 테스트 
arr = [5, 2, 4, 6, 1, 3]
sorted_arr = merge_sort(arr)
print("정렬된 결과:", sorted_arr)


        