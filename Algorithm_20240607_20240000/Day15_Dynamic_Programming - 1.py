"""

    * 15장 개요 
    - 동적 계획법(DP)은 복잡한 문제를 작은 부분 문제로 나누고, 이미 해결한 부분 문제의 결과를 저장하여 동일한 문제를 다시 계산하지 않도록 하는 알고리즘 기법이다. 
    
    * 학습 내용 
    1. 동적 계획법 개념 및 원리 
    2. 메모이제이션(Memoization)과 탑다움/바텀업 접근 방식 
    3. 대표적인 DP 문제 풀이 
        - 피보나치 수열 
        - 최소 동전 개수 문제 
        - 배낭 문제(Knapsack Problem)
        
"""

"""

    * 시작 예제 : 피보나치 수열 (재귀 vs DP)
    먼저, 일반적인 재귀 방식과 동적 계획법을 적용한 방식을 비교해보자. 

"""

# (비효율적인) 일반 재귀 방식 
def fib_recursive(n):
    if n<= 1:
        return n 
    return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(10)) # 55 
# ==> 중복 계산이 많아 시간 복잡도O(2^n)으로 매우 비효율적이다. 


# (효율적인) 메모이(제이션을 활용한 DP 방식
def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n-1,memo) + fib_memoization(n-2,memo)
    return memo[n]

print(fib_memoization(10)) # 55
# ==> 이전 계산 값을 저장하여 시간 복잡도O(n)으로 개선됨. 
