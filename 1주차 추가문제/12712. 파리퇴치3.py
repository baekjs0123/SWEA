import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0 , -1, 0]
    cnt = 0
    for r in range(N):
        for c in range(N):
            for d in range(4):
                for k in range(1, M):
                    nr = r + dr[d]*k
                    nc = c + dc[d]*k
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]
    print(cnt)




    # def killfly_vertical(field, x, y, m):
    #     '''
    #     필드와 x,y 좌표, 스프레이 길이 m을 받아서
    #     해당 좌표에서 상하좌우 m칸의 파리 킬수를 합산해서 리턴하는 함수
    #     '''
    #     kills = 0
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #     for dx, dy in directions:
    #         for k in range(1, m):
    #             nx = x + dx * k
    #             ny = y + dy * k
    #             if 0 <= nx < n and 0 <= ny < n:
    #                 kills += field[nx][ny]
    #
    #     return kills + field[x][y]
    #
    #
    # def killfly_diognal(field, x, y, m):
    #     '''
    #     필드와 x,y 좌표, 스프레이 길이 m을 받아서
    #     해당 좌표에서 대각선 4방향 m칸의 파리 킬수를 합산해서 리턴하는 함수
    #     '''
    #     kills = 0
    #     directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    #     for dx, dy in directions:
    #         for k in range(1, m):
    #             nx = x + dx * k
    #             ny = y + dy * k
    #             if 0 <= nx < n and 0 <= ny < n:
    #                 kills += field[nx][ny]
    #
    #     return kills + field[x][y]
    #
    #
    # kills_max = 0
    #
    # for i in range(n):
    #     for j in range(n):
    #         kills_vertical = killfly_vertical(field, i, j, m)
    #         kills_diagnol = killfly_vertical(field, i, j, m)
    #
    #         if kills_max < kills_vertical:
    #             kills_max = kills_vertical
    #
    #         if kills_max < kills_diagnol:
    #             kills_max = kills_diagnol
    #
    # print(kills_max)

# 특정 숫자(문자)의 위치찾기
# pos = [(i,j) for i in range(세로) for j in range(가로) if arr[i][j] == "문자"]

# 벽 막히면 중단

# for dx, dy in directions:
#             for k in range(1,m):
#                 nx = x+dx*k
#                 ny = y+dy*k

#                 if field[nx][ny] = "벽":
#                    break
#                 if 0<= nx < n and 0<= ny <n:
#                    kills += field[nx][ny]

# 특정 숫자(문자)의 위치찾기
# pos = [(i,j) for i in range(세로) for j in range(가로) if arr[i][j] == "문자"]

# 벽 막히면 중단

# for dx, dy in directions:
#             for k in range(1,m):
#                 nx = x+dx*k
#                 ny = y+dy*k

#                 if field[nx][ny] = "벽":
#                    break
#                 if 0<= nx < n and 0<= ny <n:
#                    kills += field[nx][ny]

    # 특정 숫자(문자)의 위치찾기
    # pos = [(i,j) for i in range(세로) for j in range(가로) if arr[i][j] == "문자"]

    # 벽 막히면 중단

    # for dx, dy in directions:
    #             for k in range(1,m):
    #                 nx = x+dx*k
    #                 ny = y+dy*k

    #                 if field[nx][ny] = "벽":
    #                    break
    #                 if 0<= nx < n and 0<= ny <n:
    #                    kills += field[nx][ny]

    # N, M = map(int, input().split())
    # # N : 배열의 크기
    # # M : 스프레이의 세기
    #
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # # 만약 파리채 위치가 a로 주어질 경우에는
    # pos_killer = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 'a']
    #
    #
    # def killfly_vertical(x, y, m):
    #     '''
    #     필드와 x,y 좌표, 스프레이 길이 m을 받아서
    #     해당 좌표에서 상하좌우 m칸의 파리 킬수를 합산해서 리턴하는 함수
    #     '''
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #     kills = 0
    #
    #     for dx, dy in directions:
    #         for k in range(1, m):
    #             nx = x + dx * k
    #             ny = y + dy * k
    #             if 0 <= nx < N and 0<= ny < N:
    #                 kills += arr[nx][ny]
    #     return kills
    #
    #
    # def killfly_diognal(x, y, m):
    #     '''
    #     필드와 x,y 좌표, 스프레이 길이 m을 받아서
    #     해당 좌표에서 대각선 m칸의 파리 킬수를 합산해서 리턴하는 함수
    #     '''
    #     directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    #     kills = 0
    #     for dx, dy in directions:
    #         for k in range(1, m):
    #             nx = x + dx * k
    #             ny = y + dy * k
    #             if 0 <= nx < N and 0<= ny < N:
    #                 kills += arr[nx][ny]
    #     return kills += arr[nx][ny]
    #
    #
    # kill_max = 0
    # for i in range(N):
    #     for j in range(N):
    #         kills_vertical = killfly_vertical(i, j, M)
    #         kills_diognal = killfly_diognal(i, j, M)
    #         if kill_max < kills_vertical:
    #             kill_max = kills_vertical
    #         if kill_max < kills_diognal:
    #             kill_max = kill_max
    # print(f'#{tc} {kill_max}')
    # # 최대로 잡을 수 있는 파리 수
    # max_fly = 0
    #
    # # 상하좌우 델타탐색 1번
    # di = [-1, 1, 0, 0]
    # dj = [0, 0, -1, 1]
    # # 대각선 4방향 델타탐색 2번
    # di = [-1, -1, 1, 1]
    # dj = [1, -1, -1, 1]

    # 그 중에 최대값 구해서 출력

    # print(f'')
