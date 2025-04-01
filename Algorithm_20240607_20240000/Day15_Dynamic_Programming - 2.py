
"""
    0/1 배낭 문제 (Knapsack Problem)
    
    문제 설명 
    - 무게 제한이 W인 배낭이 있음. 
    - n개의 아이템이 주어지며, 각 아이템은 무가 weight[i]와 가치 value[i]를 가짐. 
    - 배낭에 넣을 수 있는 최대 가치를 구해야 함. 
    - 아이템은 한 번만 선택 가능 (부분 배낭 문제와 다름).
"""

# 재귀적 접근 
# 재귀적으로 모든 경우를 탐색할 수 있음.
# dp(i,w) : i번째 물건가지 고려했을 때, 배낭 용량이 w일 때 얻을 수 있는 최대 가치 

def knapsack_recursive(weights, values, W, n):
    if n == 0 or W == 0:
        return 0 # 배낭이 비거나, 더 이상 선택할 아이템이 없으면 0 반환 
    
    if weights[n-1] > W:
        return knapsack_recursive(weights, values, W, n -1) # 현재 아이템이 너무 무거우면 제외 
    
    # 현재 아이템을 포함하는 경우 vs 포함하지 않는 경우 
    include = values[n-1] + knapsack_recursive(weights, values, W - weights[n-1], n-1)
    exclude = knapsack_recursive(weights, values, W, n-1)
    
    return max(include, exclude) # 둘 중 더 큰 값 선택 

# 예제 데이터 
weights = [2,3,4,5]
values = [3,4,5,6]
W=5 
n=len(weights)

print(knapsack_recursive(weights, values, W, n)) # 출력 : 7 
# 시간 복잡도 : O(2^n) -> 모든 경우를 탐색하므로 매우 비효율적! 


# 동적 계획법 (DP) - 상향식 접근
# 중복 계산을 피하기 위해 2D DP 테이블 사용 
# dp[i][w] -> i번째 아이템가지 고려했을 때, 배낭 용량이 w일 때 얻을 수 있는 최대 가치  

def knapsack_dp(weights, values, W):
    n = len(weights)
    dp = [[0] * (W+1) for _ in range(n + 1)] # DP 테이블 초기화 
    
    for i in range(1,n+1):
        for w in range(W+1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w] # 현재 아이템을 담을 수 없으면 이전 값 유지 
            else:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
                
    return dp[n][W]   

# 예제 실행
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)

print(knapsack_dp(weights, values, W)) # 출력 : 7
# 시간 복잡도 : O(n*W)
# 공간 복잡도 : O(n*W) (공간 최적화 가능)


# 공간 최적화 DP (1D 배열 사용)
# 2D 배열 대산 1D 배열을 이용하여 공간을 O(W)로 줄일 수 있음. 
def knapsack_optimized(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1) # 1D DP 배열
    
    for i in range(n):
        for w in range(W, weights[i] - 1, -1): # 뒤에서부터 업데이트 
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[W]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)
print(knapsack_optimized(weights, values, W)) # 출력 : 7
# 시간 복잡도 : O(n*W)
# 공간 복잡도 : O(W)


""" 
    다음은? 
    - 배분 배낭 문제 (Fractional Knapsack) -> 그리디 알고리즘 적용 
    - 다차원 배낭 문제 (Multi-dimensional Knapsack)
    - 배낭 문제 변형 (Subset Sum, Unbounded Knapsack, 등등)
"""    
    




