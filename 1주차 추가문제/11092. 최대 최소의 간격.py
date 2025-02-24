T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_i = 0
    max_i = 0
    min_num = arr[0]
    max_num = arr[0]
    for i in range(len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]
            min_i = i
        if max_num <= arr[i]:
            max_num = arr[i]
            max_i = i
    result = abs(max_i - min_i)
    print(f'#{tc} {result}')