import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    paint_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(paint_arr)
    for i in range(len(paint_arr)):
        for j in range(len(paint_arr[i])):
            arr[j][j] = 1

    cnt = 0
    for i in range(len(paint_arr)):
        r1, c1 = paint_arr[i][0], paint_arr[i][1]
        r2, c2 = paint_arr[i][2], paint_arr[i][3]
        color = paint_arr[i][4]
        for j in range(len(arr)):
            for k in range(len(arr[j])):
                if arr[j][k] == 0:
                    if r1 <= k <= r2 and c1 <= j <= c2:
                        arr[j][k] = color
                else:
                    if r1 <= k <= r2 and c1 <= j <= c2:
                        cnt += 1
    print(f'#{tc} {cnt}')




