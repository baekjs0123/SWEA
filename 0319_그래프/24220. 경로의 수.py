import sys
sys.stdin = open('input.txt', 'r')

def dfs(graph, current, goal, visited):
    """
    깊이 우선 탐색(DFS)을 사용하여 현재 정점에서 목표 정점까지의 모든 경로를 찾습니다.

    :param graph: 그래프를 나타내는 인접 리스트
    :param current: 현재 정점
    :param goal: 목표 정점
    :param visited: 방문한 정점을 추적하는 리스트
    :return: 경로의 수
    """
    # 현재 정점을 방문 처리합니다.
    visited[current] = True

    # 현재 정점이 목표 정점과 같다면 경로를 찾은 것이므로 1을 반환합니다.
    if current == goal:
        visited[current] = False
        return 1

    # 경로의 수를 저장할 변수를 초기화합니다.
    path_count = 0

    # 현재 정점에 인접한 모든 정점을 탐색합니다.
    for neighbor in graph[current]:
        # 인접한 정점을 아직 방문하지 않았다면 재귀적으로 DFS를 수행합니다.
        if not visited[neighbor]:
            path_count += dfs(graph, neighbor, goal, visited)

    # 현재 정점의 방문을 해제하여 다른 경로에서 방문할 수 있도록 합니다.
    visited[current] = False

    return path_count

def count_paths(N, E, edges, S, G):
    """
    주어진 그래프에서 출발점 S에서 도착점 G까지 각 정점을 한 번씩만 방문하여 도달할 수 있는 모든 경로의 수를 계산합니다.

    :param N: 정점의 수
    :param E: 간선의 수
    :param edges: 간선 목록 (출발 정점, 도착 정점)
    :param S: 출발 정점
    :param G: 도착 정점
    :return: 가능한 경로의 수
    """
    # 그래프를 인접 리스트로 표현합니다.
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append(v)

    # 방문 여부를 추적하는 리스트를 초기화합니다.
    visited = [False] * (N + 1)

    # DFS를 사용하여 모든 경로의 수를 계산합니다.
    return dfs(graph, S, G, visited)

# 테스트 케이스를 처리합니다.
T = int(input())
for tc in range(1, T + 1):
    # 정점의 수 N과 간선의 수 E를 입력받습니다.
    N, E = map(int, input().split())

    # 간선 정보를 입력받습니다.
    edges = []
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append((u, v))

    # 출발 정점 S와 도착 정점 G를 입력받습니다.
    S, G = map(int, input().split())

    # 가능한 경로의 수를 계산합니다.
    result = count_paths(N, E, edges, S, G)

    # 결과를 출력합니다.
    print(f'#{tc} {result}')

