import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N: 숫자열 A의 길이, M: 숫자열 B의 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = -200      # 문제 조건 고려
    if N < M :
        N, M = M, N
        A, B = B, A
    if N > M: #인 경우에 대한 코드
        for i in range(N - M + 1): # 긴 배열에서 기준 위치 i
            s = 0                   # 기준 위치부터 마주보는 원소들의 곱의 합
            for j in range(M):      # 짧은 배열에서 비교하는 위치
                s += A[i+j] * B[j]       # 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때
            if max_v < s:
                max_v = s
    print(f'#{tc} {max_v}')