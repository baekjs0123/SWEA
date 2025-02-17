import sys
sys.stdin = open('input.txt', 'r')

def vertical(i, j, N):
    # 세로(상하) 검사
    count = 1
    for d in [1, -1]:
        for k in range(1, N):
            ni = i + d * k
            if ni < 0 or ni >= N:
                break
            if arr[ni][j] == 'o':
                count += 1
            else:
                break
    if count >= 5:
        return 'YES'

    # 가로(좌우) 검사
    count = 1
    for d in [1, -1]:
        for k in range(1, N):
            nj = j + d * k
            if nj < 0 or nj >= N:
                break
            if arr[i][nj] == 'o':
                count += 1
            else:
                break
    if count >= 5:
        return 'YES'

    return 'NO'


def diognal(i, j, N):
    # 주 대각선(좌상 ~ 우하) 검사
    count = 1
    for d in [1, -1]:
        for k in range(1, N):
            ni = i + d * k
            nj = j + d * k
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                break
            if arr[ni][nj] == 'o':
                count += 1
            else:
                break
    if count >= 5:
        return 'YES'

    # 부 대각선(우상 ~ 좌하) 검사
    count = 1
    for (di, dj) in [(1, -1), (-1, 1)]:
        for k in range(1, N):
            ni = i + di * k
            nj = j + dj * k
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                break
            if arr[ni][nj] == 'o':
                count += 1
            else:
                break
    if count >= 5:
        return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    result = 'NO'
    # 모든 돌에 대해 검사하되, 한 번이라도 YES가 나오면 반복 종료
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if vertical(i, j, N) == 'YES' or diognal(i, j, N) == 'YES':
                    result = 'YES'
                    break
        if result == 'YES':
            break
    print(f'#{tc} {result}')