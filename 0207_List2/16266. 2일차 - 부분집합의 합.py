import sys

sys.stdin = open("../0211_String/sample_input.txt", "r")

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # N = 부분 집합 원소의 수
    # K = 원소의 합
    count = 0
    for i in range(1 << 12):
        ith_subset_sum = 0
        ith_subset = []
        for j in range(12):
            if i & (1 << j):
                ith_subset_sum += A[j]
                ith_subset.append(A[j])

        if ith_subset_sum == K and len(ith_subset) == N:
            count += 1
    print(f'#{tc} {count}')

