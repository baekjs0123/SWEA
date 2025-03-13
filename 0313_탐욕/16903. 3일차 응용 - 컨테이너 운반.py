# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    # Wi: 화물의 무게, ti: 트럭의 적재용량
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    '''
    화물 무게가 최대가 되어야 하므로 무거운 순으로 정렬한다.
    정렬 후 옮길 수 있으면 한개씩 옮긴다.
    '''
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    max_total_wight = 0
    truck_index = 0

    # 가장 무거운 컨테이너부터 순서대로 트럭에 적재
    for weight in wi:
        if truck_index < M and weight <= ti[truck_index]:
            max_total_wight += weight
            truck_index += 1

    print(f"#{tc} {max_total_wight}")


