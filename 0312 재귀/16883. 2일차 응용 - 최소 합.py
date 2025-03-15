# import sys
#
# sys.stdin = open('input.txt', 'r')

# 우 하
dr = [0, 1]
dc = [1, 0]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

# 행번호, 열번호
# 현재 (r, c) 까지 오는데 더한 숫자들 : now_sum
def solve(r, c, now_sum):
    global min_sum

    # 1. 종료조건
    # 내 현재 위치가 (N-1, N-1)
    if (r, c) == (N-1, N-1):
        # 최소값 계산
        if min_sum > now_sum:
            min_sum = now_sum
    # 2. 재귀 호출
    # 종료 조건에 가까워 지도록
    # 종료 조건에 가까워 진다는 것은
    # 오른쪽 또는 아래 가능한 방향으로 이동
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc):
            solve(nr, nc, now_sum + arr[nr][nc])

    # or
    # solve(우)
    # solve(왼)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 2차원 배열 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최소합
    min_sum = 9999999

    # 재귀 호출
    solve(0, 0, arr[0][0])

    print(f'#{tc} {min_sum}')