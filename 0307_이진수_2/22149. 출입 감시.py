# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # N: id의 개수
    person_id = list(map(int, input().split()))
    xor = 0
    for i in range(N):
        xor = xor ^ person_id[i]
    print(f'#{tc} {xor}')