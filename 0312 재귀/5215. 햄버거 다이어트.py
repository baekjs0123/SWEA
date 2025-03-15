# import sys
#
# sys.stdin = open('input.txt', 'r')


def solve(idx, sum_taste, sum_cal):
    # 칼로리 제한을 초과하면 해당 경로는 무효
    if sum_cal > L:
        return 0

    # 모든 재료를 고려한 경우, 현재까지의 맛 점수를 리턴
    if idx == N:
        return sum_taste

    # 1. 현재 재료를 선택하지 않는 경우
    not_take = solve(idx + 1, sum_taste, sum_cal)

    # 2. 현재 재료를 선택하는 경우
    take = solve(idx + 1, sum_taste + tastes[idx], sum_cal + calories[idx])

    # 두 경우 중 더 큰 맛 점수를 리턴
    return max(not_take, take)


# 메인 실행 부분: 입력 받고 결과 출력
T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    tastes = []
    calories = []
    result = 0
    for i in range(N):
        Ti, Ki = map(int, input().split())
        tastes.append(Ti)
        calories.append(Ki)

    # solve() 함수가 계산한 최대 맛 점수를 리턴
    result = solve(0, 0, 0)
    print(f"#{tc} {result}")
