import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split()) # N: 노드 갯수, M: 리프 노드 갯수, L: 출력할 노드 번호
    leaf_node_list = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M, L)
    # print(leaf_node_list)
    '''
    부모 노드번호는 자식 노드 번호 // 2 이다. 
    왼쪽 자식과 오른쪽 자식을 구별하고 그 둘의 합을 부모 노드 위치에 넣는다.
    '''
    tree = [0] * (N + 1)
    pi = 0
    for i in range(M):
        ci = leaf_node_list[i][0]
        pi = ci // 2
        c_value = leaf_node_list[i][1]
        tree[ci] = c_value
        cleft = 0
        cright = 0
        if ci % 2:
            cright = c_value
        else:
            cleft = c_value
        for j in range(-1, -(N + 1)):
            if ci % 2:
                tree[pi] += cright
            else:
                tree[pi] += cleft
    print(f'#{tc} {tree[L]}')