import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0     # 가로, 세로로 연속한 1이 K개인 경우
    # 가로로 연속한 1의 개수가 K인 경우
    cnt = 0     # 연속한 1의 개수, 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1:      # 0이거나 마지막 열이면 연속한 1의 개수 확인
                if cnt == K:
                    ans += 1
                cnt = 0         # 행 중간에 0을 만난 경우, 마지막 열에서도 초기화

    # 세로로 연속한 1의 개수가 K인 경우
    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N-1:      # 0이거나 마지막 열이면 연속한 1의 개수 확인
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans}')

    T = int(input())
    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]

        ans = 0  # 가로, 세로로 연속한 1이 K개인 경우
        # 가로로 연속한 1의 개수가 K인 경우
        cnt = 0  # 연속한 1의 개수, 초기화
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    cnt += 1
                if arr[i][j] == 0 or j == N - 1:  # 0이거나 마지막 열이면 연속한 1의 개수 확인
                    if cnt == K:
                        ans += 1
                    cnt = 0  # 행 중간에 0을 만난경우와 마지막 열에서도 초기화
        # 세로로 연속한 1의 개수가 K인 경우
        for i in range(N):
            for j in range(N):
                if arr[j][i]:
                    cnt += 1
                if arr[j][i] == 0 or j == N - 1:  # 0이거나 마지막 행이면 연속한 1의 개수 확인
                    if cnt == K:
                        ans += 1
                    cnt = 0
        print(f'#{tc} {ans}')