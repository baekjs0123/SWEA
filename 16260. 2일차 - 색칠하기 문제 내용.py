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





