import sys

sys.stdin = open('input.txt', 'r')

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

# 정사각형 방 - 정답 코드
# 접근법
# - N*N visited 배열을 만든다
# - 해당 숫자에서 갈 수 있다면 1을 기록한다.
# - 연속된 1의 길이가 가장 긴 곳이 정답이다.
# - 같은 길이가 있다면, 작은 수가 정답 위치

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)

    # 현재 위치 숫자 기준 상하좌우 확인
    # -> 1 큰 곳이 있다면 visited 기록
    for r in range(N):
        for c in range(N):
            for i in range(4):  # 상하좌우 확인
                nr = r + dr[i]
                nc = c + dc[i]
                # 델타는 범위 밖을 잘 체크 해주어야 한다.
                if is_valid(nr, nc):
                    if arr[nr][nc] == arr[r][c] + 1:
                        # 현재 숫자는 다음으로 이동이 가능하다.
                        visited[arr[r][c]] = 1
                        break   # 나머지 방향은 볼 필요 없다.
    # print(visited)
    max_cnt = cnt = start = 0
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0
    print(f'#{tc} {start} {max_cnt + 1}')
