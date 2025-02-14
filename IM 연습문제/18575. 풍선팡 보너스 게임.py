import sys
sys.stdin = open('input.txt', 'r')

def bonus_score(N, arr):
    # 각 행의 합을 미리 계산합니다.
    row_sums = [sum(row) for row in arr]

    # 각 열의 합을 계산합니다.
    col_sums = [sum(arr[i][j] for i in range(N)) for j in range(N)]

    # 각 셀에서 풍선을 터트렸을 때의 점수를 저장할 리스트 초기화
    scores = []

    # 모든 셀에 대해 점수를 계산합니다.
    for i in range(N):
        for j in range(N):
            # (i, j) 셀의 점수는 행합 + 열합 - 해당 셀의 값
            score = row_sums[i] + col_sums[j] - arr[i][j]
            scores.append(score)

    # 최대 점수와 최소 점수의 차이가 최대 보너스 점수입니다.
    return max(scores) - min(scores)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bonus_score(N, arr)}')
