import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    '''
    접근법
    각 행, 열을 순회하며 칸이 흰색(요소의 값이 1일 때)인 경우를 모두 더한다.
    모두 더한 값이 K와 일치하면 cnt += 1 을 한다.
    '''
    cnt = 0
    for i in range(N):
        for j in range(N):
            is_valid = puzzle[i][j: j + K]
            if 0 not in is_valid and len(is_valid) == K:
                print(tc, puzzle[i][j: j + K])
                cnt += 1
    print(f'#{tc} {cnt}')
