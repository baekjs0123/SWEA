T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_arr = list(map(int, input()))
    max_cnt = 0
    cnt = 1
    for i in range(len(n_arr)):
        if (i + 1) < N and n_arr[i] == 1 and n_arr[i + 1] == 1:
            cnt += 1
        if (i + 1) < N and n_arr[i + 1] == 0:
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
    print(f'#{tc} {max_cnt}')