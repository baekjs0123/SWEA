import sys

sys.stdin = open('input.txt', 'r')

# boss = [0] * 10

def find_set(n):
    if boss[n] == 0: return n   # 가리키는 보스가 0이면 n이 최종 보스
    result = find_set(boss[n]) # 재귀 호출
    boss[n] = result # 경로 압축
    return result

# t2의 boss가 t1의 boss 밑으로 들어간다.
def union_set(t1, t2):
    a = find_set(t1) # a는 t1의 boss
    b = find_set(t2) # b는 t2의 boss
    if a == b: return  # 보스가 같으면 같은 그룹이기 때문에, 탈락
    boss[b] = a # b의 boss가 a다.

# N = int(input())
# for _ in range(N):
#     a, b = map(int, input().split())
#     union_set(a, b) # a와 b가 같은 그룹
#
# M = int(input())
# for _ in range(M):
#     a, b = map(int, input().split())
#     # 보스가 같으면 같은 그룹이다
#     if find_set(a) == find_set(b): print('같은 그룹이다.')
#     else: print('다른 그룹이다.')


T = int(input())
for tc in range(1, T + 1):
    # N은 1번부터 N번까지, M : 신청서 개수
    N, M = map(int, input().split())
    boss = [0] * (N + 1) # 1번 인덱스부터 쓸거다
    numbers = list(map(int, input().split()))

    for i in range(0, len(numbers), 2):
        a, b = numbers[i], numbers[i + 1]
        union_set(a, b)
    groups = set()

    for i in range(1, N + 1):
        groups.add(find_set(i))

    print(f'#{tc} {len(groups)}')

g = [
    [0,2,6,3,0,0],
    [2,0,7,4,0,0],
    [6,7,0,0,0,0],
    [3,4,2,0,0,0],
    [0,0,1,0,0,7],
    [0,0,0,0,0,0]
]



