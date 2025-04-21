"""
    
    * 16일차 : 동적 계획법(DP) 심화
    
    오늘 배울 내용 
    1. 피포나치 수열 복습 - Top-down & Bottom-up
    2. 최장 공통 부분 수열 (LCS)
    3. 최장 증가 부분 수열 (LIS)
    4. 동전 거스름돈 문제 (Coint Change)
    5. 경로 찾기 문제 (Unique Paths)

"""

# # 1. 피보나치 수열 복습 
# ## 재귀 방식 (Top-down) + 메모이제이션
# def fib_memo(n, memo={}):
#     # 메모이제이션을 통해 이미 계산한 결과가 있으면 바로 반환 
#     if n in memo:
#         return memo[n]
    
#     # 기본 케이스 : 0 또는 1은 자기 자신 반환 
#     if n <= 1:
#         return n 
    
#     # 재귀적으로 계산한 후 메모에 저장
#     memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

#     return memo[n]


# ## 반복문 방식 (Bottom-up)
# def fib_bottom_up(n):
#     # n이 0 또는 1일 경우는 그대로 반환 
#     if n <= 1:
#         return n
    
#     # 결과 저장용 DP 테이블 생성 
#     dp = [0] * (n+1)
#     dp[1] = 1 # 초기 조건 설정: fib(0) = 0, fib(1) = 1

#     # 작은 문제부터 차근차근 계산 
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]

#     return dp[n] # 최종 결과 반환 


# # 2. 최장 공통 부분 수열 (LCS)
# def lcs(str1, str2):
#     m, n = len(str1), len(str2)

#     # DP 테이블 초기화 (m+1) x (n+1)
#     dp = [[0] * (n+1) for _ in range(m+1)]

#     # 문자열의 각 문자에 대해 비교 
#     for i in range(m):
#         for j in range(n):
#             if str1[i] == str2[j]:
#                 # 문자가 같으면 대각선 위 + 1
#                 dp[i+1][j+1] = dp[i][j] + 1
#             else:
#                 # 다르면 왼쪽과 위쪽 중 큰 값 사용 
#                 dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
#     # 최종적으로 구한 고통 부분 수열의 길이 변환 
#     return dp[m][n] 


# 3. 동전 교환 문제 (Coin Change Problem)
"""
    * 문제 설명 
    - 여러가지 종류의 동전이 주어졌을 때, 주어진 금액을 만들 수 있는 최소 동전 개수를 구하라. 
    - 각 동전은 무한히 사용 가능하다. 

    * 예시 
    coins = [1,2,5]
    amount = 11 
    -> 11을 만들 수 있는 최소 동전 개수는 3(5+5+1)
"""

## 파이썬 코드 with 주석 (Bottom-Up방식)
def coin_change(coins, amount):
    # amount + 1로 초기화한 DP 테이블 생성 (불가능한 큰 값으로 초기화)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 # 0원을 만들기 위해 필요한 동전 개수는 0개 

    # 모든 금액에 대해 최소 동전 개수 계산 
    for coin in coins:
        for x in range(coin, amount + 1):
            # 현재 금액 x에서 coin을 뺀 금액의 최솟값 + 1
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # amount 금액에 대한 값이 여전히 무한이면 만들 수 없는 경우 
    return dp[amount] if dp[amount] != float('inf') else -1

## 예제 실행 
coins = [1,2,5]
amount = 11
print("최소 동전 개수:", coin_change(coins, amount)) # 결과: 3

