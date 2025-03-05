# v번 노드 연산자를 계산 하는 함수, 숫자라면 안하기...
# v번 노드 계산 결과 알고 싶으면...왼쪽자식 결과, 오른쪽자식 결과가 필요
def solve(v):
    # 왼쪽 자식 오른쪽 자식이 없을 수 있으니...
    if v is None:
        return
    solve(tree[v][0])
    solve(tree[v][1])

    if type(tree[v][2]) is not int: # 연산자라면
        if tree[v][2] == '*':
            tree[v][2] = tree[tree[v][0]][2] * tree[tree[v][1]][2]
        elif tree[v][2] == '/':
            tree[v][2] = tree[tree[v][0]][2] / tree[tree[v][1]][2]
        elif tree[v][2] == '+':
            tree[v][2] = tree[tree[v][0]][2] + tree[tree[v][1]][2]
        else:
            tree[v][2] = tree[tree[v][0]][2] - tree[tree[v][1]][2]


for tc in range(1, 11):
    N = int(input())
    tree = [[None, None, None] for _ in range(N + 1)]
    for _ in range(N):
        # 정점정보 노드번호, 값, 왼쪽, 오른쪽
        #         node[0] node[1], node[2], node[3]
        node = input().split()
        if node[1] in '*/+-': # 연산자면 입력 4개
            tree[int(node[0])][2] = node[1]
            tree[int(node[0])][0] = int(node[2])  # 왼쪽
            tree[int(node[0])][1] = int(node[3])  # 오른쪽
        else:  # 입력 2개 노드번호, 정수
            tree[int(node[0])][2] = int(node[1])
    print(tree)

    solve(1)
    print(f'#{tc} {int(tree[1][2])}')
