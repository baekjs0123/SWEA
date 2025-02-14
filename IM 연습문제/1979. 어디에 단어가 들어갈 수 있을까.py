import sys
sys.stdin = open('input.txt', 'r')

def cnt_puzzle(N, K, puzzle):
    ans = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N - 1:  # 0이거나 마지막 열이면 연속한 1의 개수 확인
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 퍼즐을 전치시킨다
    col_puzzle = list(zip(*puzzle))
    # 함수를 활용하여 더해준다
    result = cnt_puzzle(N, K, puzzle) + cnt_puzzle(N, K, col_puzzle)

    print(f'#{tc} {result}')
