def inorder(t):
    if left[t]:
        inorder(left[t] - 1)
    result.append(c[t])
    if right[t]:
        inorder(right[t] - 1)


for tc in range(1, 11):
    N = int(input())
    c = [0] * N # c: 알파벳 담는 곳
    left = [0] * N # 왼쪽
    right = [0] * N # 오른쪽
    result = [] # 결과값
    for i in range(N):
        node = input().split()
        c[i] = node[1]
        if len(node) > 2:
            left[i] = int(node[2])
        if len(node) > 3:
            right[i] = int(node[3])
    inorder(0)
    print(f'#{tc} {"".join(result)}')

