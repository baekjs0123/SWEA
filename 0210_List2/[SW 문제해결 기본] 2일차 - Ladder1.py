def is_valid(r, c):
    """
    주어진 좌표 (r, c)가 사다리 범위 내에 있고,
    해당 위치에 사다리가 있는지 확인한다.
    """
    return 0 <= r < 100 and 0 <= c < 100 and ladder[r][c] == 1


# 0:좌 => 1:우 => 2:상
dr = [0, 0, -1]
dc = [-1, 1, 0]

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점(2)의 위치 찾기
    for c in range(100):
        if ladder[99][c] == 2:
            goal_idx = c

    # 현재 위치를 도착 지점으로 설정
    r, c = 99, goal_idx

    # 맨 위 행에 도달할 때까지 반복
    while r > 0:
        # 좌우 방향 우선 검사
        if is_valid(r, c - 1):  # 왼쪽에 사다리가 있는 경우
            while is_valid(r, c - 1):
                c -= 1
            r -= 1  # 좌우 이동 후 위로 한 칸 이동
        elif is_valid(r, c + 1):  # 오른쪽에 사다리가 있는 경우
            while is_valid(r, c + 1):
                c += 1
            r -= 1  # 좌우 이동 후 위로 한 칸 이동
        else:
            r -= 1  # 좌우에 사다리가 없으면 위로 이동

    # 결과 출력
    print(f'#{tc} {c}')