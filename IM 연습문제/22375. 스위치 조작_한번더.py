T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    default_switch = list(map(int, input().split()))
    changed_switch = list(map(int, input().split()))
    # print(default_switch, changed_switch)
    cnt = 0
    for i in range(N):
        if default_switch[i] != changed_switch[i]:
            cnt += 1
            for j in range(i, N):
                if default_switch[j]:
                    default_switch[j] = 0
                else:
                    default_switch[j] = 1
    print(f'#{tc} {cnt}')



