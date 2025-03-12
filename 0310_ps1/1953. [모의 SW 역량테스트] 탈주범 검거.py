# import sys
#
# sys.stdin = open('input.txt', 'r')

from collections import deque

# 1.BFS로 접근
# - 이동방향 : 상하좌우
# - 이동이 불가능한 케이스
#   - [델타 배열 기본] 범위 밖으로 나가면 못감
#   - [방문 기록 기본] 이미 방문한 곳은 안감
#   - [문제 조건]
#       - 현재 내 위치에서 뚫려있는 곳으로만 이동 가능
#       - 다음 가려는 곳의 터널이 뚫려있는 곳으로만 이동 가능
#       -> 이런 케이스는 델타 배열 순서와 동일하게, 이동 가능여부를 기록해두면 좋다
# 2. 방문 기록을 해야한다. (visited)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 터널들의 종류
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}


def bfs(R, C):
    dq = deque([(R, C)])    # 후보군
    visited[R][C] = 1   # 출발점 초기화

    while dq:
        nowy, nowx = dq.popleft()
        dirs = types[tunnel_map[nowy][nowx]]

        for i in range(4):
            if dirs[i] == 0:
                continue
            new_y = nowy + dy[i]
            new_x = nowx + dx[i]

            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue
            if visited[new_y][new_x]:
                continue
            if tunnel_map[new_y][new_x] == 0:
                continue

            next_dirs = types[tunnel_map[new_y][new_x]]

            if i % 2 == 0 and next_dirs[i + 1] == 0:
                continue
            if i % 2 == 1 and next_dirs[i - 1] == 0:
                continue

            visited[new_y][new_x] = visited[nowy][nowx] + 1
            dq.append((new_y, new_x))

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇 시간이 걸렸는지 기록
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0<visited[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')