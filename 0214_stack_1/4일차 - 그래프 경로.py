import sys
sys.stdin = open('sample_input.txt','r')

def dfs(S, G):
    visited = [0] * (V + 1)
    stack = []
    visited[S] = 1
    v = S
    while True:
        for w in adj_list[v]:
            if not visited[w]:
                if w == G:
                    return 1
                else:
                    stack.append(v)
                    visited[w] = 1
                    v = w
                    break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # V: 정점의 개수, E: 간선의 개수
    adj_list=[[] for _ in range(V + 1)]

    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
    S, G = map(int, input().split())
    # S: 출발 노드, G: 도착 노드
    result = dfs(S, G)
    print(f'#{tc} {result}')
