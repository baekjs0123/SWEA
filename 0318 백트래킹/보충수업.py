def dfs(lev, total):
    global ans

    if total <= ans:
        return

    if lev == N:
        ans = max(ans, total)
        return

    for i in range(N):
        # 해당 직원이 아직 일을 할당받지 않았다면
        if i not in path:
            path.append(i)
            dfs(lev + 1, total * (arr[lev][i] / 100))
            path.pop()



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    path = []
    dfs(0,1)
    result = round(ans * 100, 6)
    print(f'#{tc} {result:.6f}')