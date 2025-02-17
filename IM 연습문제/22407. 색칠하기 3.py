import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    red_r1, red_c1, red_r2, red_c2 = map(int, input().split())
    blue_r1, blue_c1, blue_r2, blue_c2 = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if red_r1 <= i <= red_r2 and red_c1 <= j <= red_c2:
                arr[i][j] = 1
            if blue_r1 <= i <= blue_r2 and blue_c1 <= j <= blue_c2:
                arr[i][j] += 2
    purple_r1 = purple_c1 = -1
    purple_r2 = purple_c2 = -1

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                if purple_r1 == -1:
                    purple_r1 , purple_c1 = i, j
                purple_r2, purple_c2 = i, j
    if purple_r1 == -1:
        print(f'#{tc} 0 0')
    else:
        print(f'#{tc} {purple_c2 - purple_c1 + 1} {purple_r2 - purple_r1 + 1}')

    # arr = [[0] * 10 for _ in range(10)]
    # a, b, c, d = map(int, input().split())
    # e, f, g, h = map(int, input().split())
    #
    # for i in range(a, c + 1):
    #     for j in range(b, d + 1):
    #         arr[i][j] = 1
    # for i in range(e, g + 1):
    #     for j in range(f, h + 1):
    #         arr[i][j] += 2
    # pi = pj = -1    # 보라색 좌상단
    # pii = pjj = -1   # 보라색 우하단
    # for i in range(10):
    #     for j in range(10):
    #         if arr[i][j] == 3:
    #             if pi ==-1:     # 좌상단을 발견한 경우
    #                 pi, pj = i, j
    #             pii, pjj = i, j # 우하단 찾기
    # if pi == -1:    # 보라색 영역이 없는 경우
    #     print(f'#{tc} 0 0')
    # else:
    #     print(f'#{tc} {pjj-pj+1} {pii-pi+1}')