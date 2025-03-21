# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N , K = map(int, input().split())
    hex_num = input()
    length = int(len(hex_num) / 4)
    hex_num = hex_num + hex_num[:length]
    decimal_arr = []
    for i in range(length):
        for j in range(i, N + i, length):
            decimal_num = int(hex_num[j: j + length], 16)
            decimal_arr.append(decimal_num)
    decimal_arr = list(set(decimal_arr))
    decimal_arr.sort(reverse=True)
    ans = decimal_arr[K - 1]
    print(f'#{tc} {ans}')


