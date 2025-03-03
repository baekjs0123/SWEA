T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    '''
    완전탐색을 하며 괴물이 있는 위치를 탐색한다 괴물은 값이 2이고 2를 탐색하고 그 지점을 monster로 저장하고 광선을 쏜다.
    괴물은 상하좌우로 벽이 없는 한 행렬의 끝까지 광선을 쏜다. 벽은 1이고 1을 만나지 않으면 상하좌우로 지나가는 모든 요소의 값을 3으로 바꿔준다.
    새로 이중 for문을 돌면서 행렬의 요소가 0인것은 카운트하여 cnt변수에 담고 출력한다.
    '''
    dr = [1,-1,0,0]
    dc = [0,0,-1,1]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                for i in range(4):
                    for k in range(1, N):
                        nr = dr[i] * k + r
                        nc = dc[i] * k + c
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 1:
                                break
                            else:
                                arr[nr][nc] = 3
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')
