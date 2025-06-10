"""

    Chapter19 : 백 트레킹 (Back tracking)
    
    1) 백트레킹 개념 
        - 백트레킹은 "모든 경우의 수를 시도하지만, 조건을 만족하지 않으면 더 이상 진행하지 않고 돌아가는 것"을 말해. 
        - 즉, 상태공간트리를 탐색하면서 "가지치기(pruning)"를 통해 불필요한 부분을 잘라냄. 
    - 예를 들어
        - N-Queens 문제 : 체스판의 퀸 배치. 가능한 경우의 수를 모두 보지만, 공격 범위에 있으면 더 이상 탐색 X. 
        - 부분집합 문제 : 집합에서 모든 부분집합을 생성. 조건을 만족하지 않으면 탐색 X. 

"""

# 2) 기본 구조 
"""
    def backtrack(state, decisions):
        if 조건을 만족하면:
            결과를 기록 
            return 
        
        for 가능한 선택 in decisions: 
            if 선택이 유효한지 확인: 
                상태 업데이트 
                backtrack(새로운 상태, 새로운 선택)
                상태 되돌리기 (backtrack)
"""

# # 기초 예제 - 부분집합 생성 
# def generate_subsets(nums):
#     result = []

#     def backtrack(start, path):
#         result.append(path[:]) # 부분집합을 저장 
#         for i in range(start, len(nums)):
#             path.append(nums[i]) # 원소 추가 
#             backtrack(i + 1, path) # 다음 원소 탐색 
#             path.pop() # 상태 복원 (백트레킹)

#     backtrack(0, [])
#     return result 

# print(generate_subsets([1,2,3]))
# # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

# 4) 심화 예제 - N-Queens 
# 크기가 n인 체스판에 n개의 퀸을 서로 공격하지 않게 배치. 
def solve_n_queens(n):
    result = []
    board = [-1] * n # 각 행위 퀸 위치 

    def is_valid(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True 
    
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return 
        for col in range(n):
            if is_valid(row, col):
                board[row] = col 
                backtrack(row + 1)
                board[row] = -1 # 상태 복원 

    backtrack(0)
    return result 

print(solve_n_queens(4))
# [[1, 3, 0, 2], [2, 0, 3, 1]]

# 5) 가지치기 (Pruning)
# 조건을 미리 체크해서 불필요한 재귀 호출을 막음. 
# 예 : N-Queens에서 같은 열이나 대각선에 퀸이 있으면 더 이상 탐색 X.

# 6) 대표 문제 
"""
    - N-Queens 
    - 부분집합 생성 
    - 순열 생성 
    - 조합 문제 
    - 미로 찾기 
"""

