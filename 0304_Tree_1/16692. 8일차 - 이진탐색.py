# import sys
# sys.stdin = open('input.txt', 'r')

def inorder(i):
    global num
    if i > N:
        return
    if 2 * i <= N:
        inorder(2 * i)
    tree[i] = num
    num += 1
    if 2 * i + 1 <= N:
        inorder(2 * i + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    '''
    중위 순회
    '''
    tree = [0] * (N + 1)
    num = 1
    inorder(1)
    root = tree[1]
    half_N_node = tree[N // 2]

    print(f'#{tc} {root} {half_N_node}')
