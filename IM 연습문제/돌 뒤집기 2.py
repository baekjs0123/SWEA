import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 돌의 수 N, 뒤집기 횟수 M
    arr = list(map(int, input().split()))  # 돌의 초기상태

    # ij = [list(map(int, input().split())) for _ in range(M)]
    for _ in range(M):
        i, j = map(int, input().split())  # i번째 돌을 사이에 두고 마주보는 j개의 돌
        i -= 1  # i 번째 돌 -> i-1 인덱스
        for k in range(1, j + 1):  # k: i번째 돌에서의 거리
            if 0 <= i - k and i + k < N:
                if arr[i - k] == arr[i + k]:  # 같은 색이면 뒤집고, 다른색이면 그대로
                    # if arr[i - k]:      # if arr[i - k] == 1:
                    #     arr[i - k] = 0
                    #     arr[i + k] = 0
                    # else:       # arr[i-k] == 0
                    #     arr[i - k] = 1
                    #     arr[i + k] = 1
                    arr[i-k] = (arr[i-k] +1 )%2     # arr[i-k] ^= 1 (1,0을 뒤집는 연산)
                    arr[i+k] = (arr[i+k] +1 )%2


    print(f'#{tc}', *arr)
