import sys
import pprint

sys.stdin = open('../0211_String/sample_input.txt', 'r')

for _ in range(10):
    T = int(input())

    arr = [[0] * 100 for _ in range(100)]
    r_sum = 0  # 각 행의 합
    c_sum = 0  # 각 열의 합
    main_diagonal_sum = 0  # 왼쪽 상단에서 오른쪽 하단으로 내려가는 대각선의 합
    anti_diagonal_sum = 0  # 오른쪽 상단에서 왼쪽 하단으로 내려가는 대각선의 합

    # print(float('inf')) : 무한대를 표현하는 법
    # print(float('-inf')) : 음의 무한대를 표현하는 법
    max_sum = 0
    for i in range(len(arr)):
        arr[i] = list(map(int, input().split()))

    for i in range(len(arr)):
        sum_nums = 0
        for j in range(len(arr[i])):
            sum_nums += arr[i][j]
        if r_sum < sum_nums:
            r_sum = sum_nums
        sum_nums = 0
        for j in range(len(arr[i])):
            sum_nums += arr[j][i]
        if c_sum < sum_nums:
            c_sum = sum_nums
        for j in range(len(arr[i])):
            if i == j:
                main_diagonal_sum += arr[i][j]
            if i + j == 100 - 1:
                anti_diagonal_sum += arr[i][j]

    max_sum = r_sum
    if max_sum < c_sum:
        max_sum = c_sum
    if max_sum < main_diagonal_sum:
        max_sum = main_diagonal_sum
    if max_sum < anti_diagonal_sum:
        max_sum = anti_diagonal_sum

    print(f'#{T} {max_sum}')
