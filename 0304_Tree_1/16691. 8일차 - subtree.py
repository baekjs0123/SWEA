T = int(input())

def preorder(t):
    global cnt
    if t:
        cnt += 1
        preorder(cleft[t])
        preorder(cright[t])


for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    n = E + 1  # 정점의 개수

    cleft = [0] * (n + 1)
    cright = [0] * (n + 1)

    cnt = 0

    for i in range(n - 1):
        p = arr[i * 2]
        c = arr[i * 2 + 1]
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c

    preorder(N)
    print(f'#{tc} {cnt}')
