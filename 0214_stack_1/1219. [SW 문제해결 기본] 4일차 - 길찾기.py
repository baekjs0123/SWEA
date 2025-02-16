import sys
sys.stdin = open('sample_input.txt', 'r')

SIZE = 100

def check_route_dfs(start, end, adj_list):
    """
    check_route_dfs 함수는 start에서 end로 가는 경로가 있는지
    DFS(깊이 우선 탐색)를 통해 확인한 뒤,
    존재하면 1을, 존재하지 않으면 0을 반환한다.
    """

    # 방문 여부를 기록하는 리스트입니다.
    # 인덱스 0부터 99까지, 총 100개의 노드가 있다고 가정하고 0으로 초기화한다.
    visited = [0] * SIZE

    # 내부에 실제 DFS를 수행하는 함수를 정의한다.
    def dfs(current_node):
        """
        dfs 함수는 current_node부터 시작해
        end 노드를 찾을 때까지 깊이 우선 탐색을 수행한다.
        :param current_node: 현재 탐색 중인 노드
        :return: end 노드를 찾으면 True, 아니면 False
        """
        # 만약 현재 노드가 목표(end) 노드라면, 경로가 존재한다고 판단하고 True를 반환한다.
        if current_node == end:
            return True

        # 아직 방문하지 않았다면 방문 체크
        visited[current_node] = True

        # 현재 노드에 연결된(갈 수 있는) 모든 자식 노드를 확인합니다.
        for next_node in adj_list[current_node]:
            # 만약 다음 노드를 아직 방문하지 않았다면
            if not visited[next_node]:
                # 해당 노드로 이동하여 DFS를 수행해봅니다.
                if dfs(next_node):
                    # dfs(next_node) 결과가 True면, end 노드를 찾았다는 의미이므로
                    # 더 이상 탐색하지 않고 True를 반환합니다.
                    return True

        # 모든 자식 노드를 탐색했음에도 end 노드를 찾지 못했다면 False를 반환합니다.
        return False

    # 실제 DFS를 시작 노드(start)에서 수행하고,
    # 결과값(True/False)에 따라 1 또는 0을 리턴합니다.
    return 1 if dfs(start) else 0


# 메인 루틴 예시
for _ in range(1, 11):
    # 테스트 케이스 번호(tc)와 간선의 개수(e)를 입력받습니다.
    tc, e = map(int, input().split())
    edges = list(map(int, input().split()))

    # 노드(도시)가 0부터 99까지 있다고 가정하고, 각 노드별로 갈 수 있는 노드를 저장할 인접 리스트를 만듭니다.
    adj_list = [[] for _ in range(SIZE)]

    # 입력받은 간선 정보를 통해 adj_list를 구성합니다.
    # 예) edges = [0, 1, 0, 2, 1, 4, 1, 3, ...] 형태로 주어졌다면
    # (0, 1), (0, 2), (1, 4), (1, 3) ... 이런 식으로 간선을 형성합니다.
    for i in range(0, 2 * e, 2):
        start_node = edges[i]
        end_node = edges[i + 1]
        adj_list[start_node].append(end_node)

    # DFS 함수를 이용해 0에서 99까지 경로가 있는지 확인합니다.
    result = check_route_dfs(0, 99, adj_list)

    # 결과를 출력합니다.
    print(f"#{tc} {result}")

