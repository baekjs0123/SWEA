import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    min_v = 400  # 가로 세로 각각 20 이하, 각 원소 10 미만

    for i in range(N):  # 터트리는 풍선의 위치
        for j in range(N):
            s = arr[i][j]  # 터트린 풍선의 점수 합계
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 각 방향별로
                for k in range(1, N):  # 거리별로
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]  # i, j 에  di, dj방향으로  k칸 떨어진 풍선
                    else:
                        break

            # 각 방향으로 점수합계가 끝나면
            if max_v < s:
                max_v = s
            if min_v > s:
                min_v = s
    print(f'#{tc} {max_v - min_v}')
