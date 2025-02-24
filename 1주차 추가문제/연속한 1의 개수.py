import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input())) + [0]
    max_cnt = 0
    cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(f'#{tc} {max_cnt}')
