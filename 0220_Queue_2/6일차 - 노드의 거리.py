from collections import deque

T = int(input())


# S : 시작정점번호
# G : 도착정점번호(목표)
# V : 정점의개수
def bfs(S, G, V):
    # 방문배열
    visited = [0] * (V + 1)
    # 내가 다음에 방문할 정점들을 순서대로 저장
    # 큐
    Q = deque()
    # 시작 처리
    Q.append(S)
    visited[S] = 1

    # 큐가 빌때까지 반복
    # 큐가 비었다는 것은 => 다음에 방문할 정점이 없다.
    # 탐색 종료

    # 거리
    distance = 0

    while Q:
        # 큐에서 다음에 방문할 정점을 빼기전에
        # 큐의 길이를 통해서 다음 단계는 몇번 반복할지
        # 구할수 있다
        size = len(Q)
        distance = distance + 1

        # 이 단계에서는 size 만큼만 반복을 한다.
        for _ in range(size):
            # 현재 정점 번호
            now = Q.popleft()

            # 현재 정점과 연결된 정점 중에서
            # 이전에 방문한적 없는 곳만 큐에 추가
            for next in g[now]:
                # next : now정점과 연결되어있는 정점
                if not visited[next]:
                    # next 정점을 나중에 방문하겠다.
                    Q.append(next)
                    visited[next] = 1
                    # next가 목표로한 정점이면
                    if next == G:
                        return distance

    # 여기까지 코드가 실행되버렸으면
    # 반복도는중에 목표 정점을 만나지 못한경우
    return 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트
    g = [[] for _ in range(V + 1)]

    # 간선의 정보 입력 받기
    for i in range(E):
        s, e = map(int, input().split())
        # s 정점에서 e정점으로 가는길이 있다.
        # s 정점과 e정점은 인접해있다.
        g[s].append(e)
        # 방향이 없는 그래프는 반대도 추가
        g[e].append(s)

    # 출발노드 S, 도착노드 G
    # 도착 가능? 최소 거리
    S, G = map(int, input().split())

    print(f"#{tc} {bfs(S, G, V)}")
