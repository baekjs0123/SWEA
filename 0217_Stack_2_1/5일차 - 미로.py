import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(si, sj):
    # 왔던 길은 다시 가지 않도록 방문체크
    # 2차원 배열은 위치정보가 2개로 표현됨(행,열)
    visited = [[0] * N for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 지나온길, 갈림길을 기억하기 위한 스택
    # 위치정보가 (i,j) 형태로 표현되기 때문에
    # 이 안에 들어갈 위치정보도(2,3)... 이런식이다.


    # 현재위치 i, j 는 시작위치 si,sj 에서 시작
    i, j = si, sj
    stack = []
    # 미로 탈출할 때 까지 반복(모든 길 탐색할 때까지)
    while True:
        # 현재 위치가 도착점인가 판별
        # print(i,j)
        # 도착점(탈출지점)을 만나면 더이상 진행할 필요 x
        if maze[i][j] == 3:
            return 1

        # 현재위치 기준 상하좌우 4방향 탐색
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 내가 계산한 이 다음 위치가 가도 되는 위치인가???
            # 1. 범위 (인덱스)
            # 2. 벽은 가면 안된다.
            # 3. 방문했던길은 가면 안된다.
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                stack.append((i, j))
                visited[ni][nj] = 1
                i, j = ni, nj
                break

        else:
            # 네방향 뒤져봤는데 갈수있는곳 없었음.
            if stack:
                # 돌아갈곳 찾아가기
                i, j = stack.pop()
            else:
                # 돌아갈곳 없었다.
                break

    # 탐색이 모두 끝나고 나니 종료지점 못만났음..
    return 0


for tc in range(1, T + 1):

    # 미로의 크기
    N = int(input())
    # 미로(2차원배열)
    maze = [list(map(int, input())) for _ in range(N)]

    # 탐색을 시작하는 정점의 위치
    # 시작 행번호, 시작 열 번호
    si = sj = 0

    # 탐색 시작 위치는 2가 있는곳
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                # 시작 위치 설정
                si, sj = i, j

    print(f"#{tc} {dfs(si, sj)}")
