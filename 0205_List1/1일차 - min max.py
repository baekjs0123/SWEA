T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):  # 케이스 별로 처리
    N = int(input())  # 케이스 별 입력 개수
    arr = list(map(int, input().split()))

    max_v = arr[0]  # 첫 원소를 최대값으로 가정
    min_v = arr[0]  # 첫 원소를 최소값으로 가정

    for i in range(1, N):
        if max_v < arr[i]:  # arr[i] > max_v (다음 연산식과 비교식 순서를 맞출 것)
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    print(f'#{tc} {max_v - min_v}')