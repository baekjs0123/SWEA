import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N: 가로길이

    # DP 배열을 초기화합니다. 인덱스 0부터 N까지 사용하므로 (N + 1) 크기로 설정합니다.
    dp = [0] * (N + 1)

    # 초기 조건을 설정합니다.
    dp[0] = 1  # 가로 길이가 0인 경우, 아무 종이도 사용하지 않는 한 가지 방법이 있습니다.
    # 동적 계획법을 사용하여 각 가로 길이 n에 대한 경우의 수를 계산합니다.
    for n in range(10, N + 1, 10):
        # 10x20 종이를 세로로 배치하는 경우
        if n >= 10:
            dp[n] += dp[n - 10]
        # 20x20 종이를 가로로 배치하는 경우
        if n >= 20:
            dp[n] += 2 * dp[n - 20]


    print(f'#{tc} {dp[N]}')
