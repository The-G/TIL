"""

    * LIS(Longest Increasing Subsequence)
    문제 설명 
    - 주어진 수열에서 오름차순으로 정렬된 가장 긴 부분 수열을 찾아 그 길이를 구하라. 
    - 수열의 일부 요소들을 건너뛰면서 만들어도 된다. 
    
"""


# # Bottom-Up방식 O(n^2)
# def length_of_lis(nums):
#     n = len(nums)
#     dp = [1] * n # 각 위치에서의 LIS 길이를 저장 
    
#     for i in range(n):
#         for j in range(i):
#             if nums[j] < nums[i]: # 증가하는 조건이면
#                 dp[i] = max(dp[i], dp[j]+1) # LIS 길이 갱신 
    
#     return max(dp) if dp else 0 # 가장 긴 LIS 길이 반환 

# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# print("LIS 길이:", length_of_lis(nums)) # 결과: 4


# # 시각화 코드 (matplotlib 사용)
# import matplotlib.pyplot as plt

# def visualize_lis(nums):
#     n = len(nums)
#     dp = [1] * n  # LIS 길이 저장
#     prev = [-1] * n  # 추적용

#     # LIS 계산 + 추적 정보 저장
#     for i in range(n):
#         for j in range(i):
#             if nums[j] < nums[i] and dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#                 prev[i] = j

#     # 최장 LIS의 인덱스 추적
#     lis_end = dp.index(max(dp))
#     lis_sequence = []
#     while lis_end != -1:
#         lis_sequence.append(lis_end)
#         lis_end = prev[lis_end]
#     lis_sequence.reverse()

#     # 시각화
#     fig, ax = plt.subplots(figsize=(12, 4))
#     x = list(range(n))
#     y = nums

#     # 전체 수열 plot
#     ax.plot(x, y, 'o-', label='Sequence', color='gray')

#     # LIS 길이 주석 추가
#     for i in range(n):
#         ax.text(x[i], y[i] + 1, f"LIS:{dp[i]}", ha='center', fontsize=10)

#     # 최장 증가 부분 수열 강조
#     lis_x = [i for i in lis_sequence]
#     lis_y = [nums[i] for i in lis_sequence]
#     ax.plot(lis_x, lis_y, 'ro-', linewidth=2.5, label='Longest Increasing Subsequence')

#     ax.set_title("LIS 시각화")
#     ax.set_xlabel("Index")
#     ax.set_ylabel("Value")
#     ax.legend()
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()

# # 예제 실행
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# visualize_lis(nums)

# 설명 
"""
    * 설명 
      - dp[i]는 i번째 수까지의 LIS 길이를 의미해. 
      - prev 배열은 실제 LIS를 역추적해서 시쿼스를 복원하는 데 사용돼. 
      - 최종적으로 LIS 수열만 빨간선으로 강조해서 표시해. 
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.font_manager as fm

# 한글 폰트 설정 - 예: 맑은 고딕
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # macOS
# plt.rcParams['font.family'] = 'NanumGothic'  # Linux (설치 필요 시 pip install nanum-font)

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

nums = [10, 9, 2, 5, 3, 7, 101, 18]

def lis_with_steps(nums):
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    steps = []

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        # 각 단계에서 현재 i까지의 LIS 경로 추적
        path = []
        idx = i
        while idx != -1:
            path.append(idx)
            idx = prev[idx]
        steps.append((dp.copy(), path[::-1]))

    return steps

def animate_lis_path(nums, steps):
    fig, ax = plt.subplots(figsize=(12, 5))
    x = list(range(len(nums)))
    y = nums

    def update(i):
        ax.clear()
        dp, path = steps[i]

        # 전체 수열 표시
        ax.plot(x, y, 'o-', color='lightgray', label='전체 수열')
        # 현재 LIS 부분 수열 표시
        ax.plot([idx for idx in path], [nums[idx] for idx in path], 'ro-', label='현재 LIS')

        for idx in range(len(nums)):
            ax.text(x[idx], y[idx] + 1, f"LIS:{dp[idx]}", ha='center', fontsize=10)

        ax.set_title(f"LIS 추적 (단계 {i + 1}/{len(steps)})")
        ax.set_ylim(0, max(nums) + 20)
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.grid(True)
        ax.legend()

    ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=1000)
    plt.tight_layout()
    plt.show()

# 실행
steps = lis_with_steps(nums)
animate_lis_path(nums, steps)


