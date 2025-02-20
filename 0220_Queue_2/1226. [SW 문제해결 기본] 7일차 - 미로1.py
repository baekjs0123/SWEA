from collections import deque

# 미로 범위 유효성 검사
def is_valid(i, j):
    return 0 <= i < 16 and 0 <= j < 16

# bfs
def bfs():
    # 방문한 구역 체크하기 위한 visited
    visited = [[0] * 16 for _ in range(16)]
    # 덱 생성
    q = deque()
    # 덱에 처음 출발 위치인 [1, 1] enqueue
    q.append([1, 1])
    # 덱에 담자마자 출발지 1로 방문했다고 체크
    visited[1][1] = 1

    while q:
        # 현재 위치 pop
        now_i, now_j = q.popleft()
        # 현재 위치가 '3'인 경우 골인
        if maze[now_i][now_j] == '3':
            # 도달 가능 여부만 출력하면 되므로 1리턴
            return 1
        # 델타 탐색하며 다음 위치 확인
        for di, dj in [[0,1],[1,0],[0, -1],[-1,0]]:
            next_i, next_j = now_i  + di, now_j + dj
            # 1. 다음 위치가 미로 범위 안이고
            # 2. 벽이 아니며
            # 3. 방문 한 적이 없을 때
            # enqueue
            if is_valid(next_i, next_j) and maze[next_i][next_j] != '1' and visited[next_i][next_j] == 0:
                # 위 조건을 만족할 때마다 enqueue
                q.append([next_i, next_j])
                # enqueue와 동시에 방문기록
                visited[next_i][next_j] += 1
    # while문이 끝날 때 까지 return을 하지 않았다는 것은
    # q가 공백일 때 까지 길을 못찾았다는 뜻 = return 0
    return  0

for _ in range(10):
    tc = int(input())
    maze = [list(map(str, input())) for _ in range(16)]
    ans = bfs()
    print(f'#{tc} {ans}')