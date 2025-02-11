T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N : 배열의 크기
    # M : 스프레이의 세기

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대로 잡을 수 있는 파리 수
    max_fly = 0

    # 상하좌우 델타탐색 1번
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 대각선 4방향 델타탐색 2번
    di = [-1, -1, 1, 1]
    dj = [1, -1, -1, 1]

    # 그 중에 최대값 구해서 출력
    print(f'')