def max_min_difference(N, M, array):
    # 초기 윈도우의 합 계산
    current_sum = sum(array[:M])
    max_sum = current_sum
    min_sum = current_sum

    # 슬라이딩 윈도우를 사용하여 합 계산
    for i in range(1, N - M + 1):
        # 새로운 합 = 이전 합 - 이전 윈도우의 첫 번째 값 + 새로운 윈도우의 마지막 값
        current_sum = current_sum - array[i - 1] + array[i + M - 1]
        # 최대값과 최소값 갱신
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum

    # 최대값과 최소값의 차이 반환
    return max_sum - min_sum

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    result = max_min_difference(N, M, array)
    print(f"#{t} {result}")