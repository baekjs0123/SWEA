# import sys
#
# sys.stdin = open('input.txt', 'r')


def find_set(n):
    if p[n] == 0:
        return n
    result = find_set(p[n])
    p[n] = result
    return result


def union_set(x, y):
    a = find_set(x)
    b = find_set(y)
    if a == b:
        return
    p[b] = a


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    p = [0] * (N + 1)

    for i in range(M):
        a, b = nums[i * 2], nums[i * 2 + 1]
        union_set(a, b)

    groups = set()
    for i in range(1, N + 1):
        groups.add(find_set(i))
    print(f'#{tc} {len(groups)}')
