# import sys
# sys.stdin = open('input.txt', 'r')

def solution():
    # N 개의 1 을 구함
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    switch = 'OFF'
    result = solution()

    if result:
        switch = 'ON'

    print(f'#{tc} {switch}')