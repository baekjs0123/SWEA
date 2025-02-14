import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 스위치 개수

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(N):  # 비교할 인덱스 i
        if A[i] != B[i]:  # 다르면 A[i] 조작
            cnt += 1
            # 상태가 바뀌는 모든 스위치 A[j], i<=j<N
            for j in range(i, N):
                if A[j]:  # if A[j] == 1:
                    A[j] = 0
                else:  # A[i] == 0이면
                    A[j] = 1

    print(f'#{tc} {cnt}')