T = int(input())
for tc in range(1, T + 1):
    '''
    접근법
    i번째 버스 노선이 Ai이상 ~ Bi이하 번호의 버스정류장에 정차한다.
    그렇다면 range(Ai, Bi + 1)만큼 반복을 돌며 bus_stop_cnt리스트에 카운트를 1씩 증가시킨다.
    그리고 range(P)만큼 반복을 돌면서 Cj의 각 요소를 확인하고 해당 번호의 정류장에
    bus_stop_cnt리스트를 통해 몇개의 노선이 지나가는지 확인하고 해당 정보를 result에 담아 준 후 출력한다.
    '''
    N = int(input())
    bus_stop = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    Cj = [int(input()) for _ in range(P)]
    bus_stop_cnt = [0] * 5000
    for i in range(len(bus_stop)):
        for j in range(bus_stop[i][0], bus_stop[i][1] + 1):
            bus_stop_cnt[j - 1] += 1
    result = []
    for i in Cj:
        result.append(bus_stop_cnt[i - 1])
    print(f'#{tc}', *result)
