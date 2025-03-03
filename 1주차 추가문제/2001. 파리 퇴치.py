# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     '''
#     이중 for문을 돌면서 델타 탐색으로 현재 칸 기준으로 델타탐색을 하지만 M이 짝수인 경우와 홀수인 경우로 나눠서 계산한다.
#     M이 홀수인 경우 현재 위치 기준으로 배열의 범위 안에서 M-2 범위 만큼 상하좌우, 대각선으로 탐색하고 그 값을 더해준다.
#     M이 짝수인 경우 현재 위치 기준으로 우,하,(i,i)대각선 방향으로 M - 1만큼 탐색하며 값을 더해준다.
#     이렇게 탐색하며 죽인 파리의 합이 max_kill보다 많아지면 max_kill을 바꿔준다.
#     '''
#     max_kill = 0
#     for r in range(N):
#         for c in range(N):
#             kill = 0
#             if M % 2 == 0:
#                 kill += arr[r][c]
#                 dr = [0, 1, 1]
#                 dc = [1, 0, 1]
#                 for i in range(3):
#                     for k in range(1, M):
#                         nr = dr[i] * k + r
#                         nc = dc[i] * k + c
#                         if 0 <= nr < N and 0 <= nc < N:
#                             kill += arr[nr][nc]
#                         if max_kill < kill:
#                             max_kill = kill
#             else:
#                 kill += arr[r][c]
#                 dr = [-1,1,0,0,-1,-1,1,1]
#                 dc = [0,0,-1,1,-1,1,-1,1]
#                 for i in range(len(dr)):
#                     for k in range(1, M - 1):
#                         nr = dr[i] * k + r
#                         nc = dc[i] * k + c
#                         if 0 <= nr < N and 0 <= nc < N:
#                             kill += arr[nr][nc]
#                         if max_kill < kill:
#                             max_kill = kill
#     print(f'#{tc} {max_kill}')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    # 가능한 모든 MxM 부분 배열을 탐색
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            kill = 0
            # MxM 부분 배열의 합 계산
            for i in range(M):
                for j in range(M):
                    kill += arr[r + i][c + j]
            # 최대값 갱신
            if max_kill < kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')
