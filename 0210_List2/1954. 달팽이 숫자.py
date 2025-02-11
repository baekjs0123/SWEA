T = int(input())


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N and snail[r][c] == 0


for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # 우 => 하 => 좌 => 상.....
    d = 0

    # 0:우 => 1:하 => 2:좌 => 3:상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 여러분이 직접 행번호와 열번호를 관리
    # r: 행번호, c: 열번호
    r, c = 0, 0
    for i in range(1, N * N + 1):
        snail[r][c] = i
        # 다음 행번호 = 현재 행번호 + d 방향으로 갔을 때 행번호의 변화량
        nr = r + dr[d]
        # 다음 열번호 = 현재 열번호  + d 방향으로 갔을 때 열번호의 변화량
        nc = c + dc[d]

        # 다음 위치가 두 조건을 만족하면 그대로 계속
        # 1. 2차원 배열 범위 안
        # 2. 숫자를 쓴적이 없음 (0)
        if is_valid(nr, nc):
            # nr, nc가 유효한 위치 => 거기로 이동
            r, c = nr, nc
        # 만약 아니라면 nr, nc는 다시 계산
        # 방향을 바꿔서 계산

        else:
            # 1
            d = (d + 1) % 4
            # 2
            # d = d + 1 if d < 3 else 0
            # 3
            # d = d + 1
            # if d > 3:
            #     d = 0

            # 방향 바꿔서 다시 계산
            r = r + dr[d]
            c = c + dc[d]
    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])
