# import sys
#
# sys.stdin = open('input.txt', 'r')


# 백트래킹 함수 (재귀)
# 현재 내가 몇칸 갈지 선택하고 있는 정류장 번호 : idx
# 현재 위치까지 오는데 충전한 횟수 : cnt
def backtracking(idx, cnt):
    global min_v
    # 0. 가지치기
    # 이전에 구한 최소 충전 횟수보다
    # 지금까지 충전한 횟수가 더 많다면 답이 될 가능성이 없음 => 돌아가기
    if cnt > min_v:
        return

    # 1. 종료 조건 : 목적지에 도착할 때까지
    # 이동 가능한 정류장 갯수가 최대 k
    # 도착 정류장이 k안에 있으면 이상황도 고려
    # 최대로 이동했을 때 도착 지점 넘어가버리면 => 그것도 도착으로 생각하자.
    if idx >= N - 1:
        # 마지막 정류장에 도착하면
        # 지금까지 충전한 횟수가 최소 충전 횟수인지 확인
        min_v = min(cnt - 1, min_v)
        return
    # 2. 재귀호출(경우의 수 나열하고 선택)
    # idx 번의 충전 용량 = bus_stop[idx]
    # 다음에 갈 수 있는 정류장 번호 : idx + 1, idx + 2 ... bus_stop[idx]

    # 현재 위치에서 최대 용량만큼 먼저 가보고 그다음에 1씩 줄여서 이동
    for i in range(bus_stop[idx], 0, -1):
        # 이동하는 정류장 개수 i
        backtracking(idx + i, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    # 한줄에 정류장 개수 N과 각 정류장의 충전용량
    line = list(map(int, input().split()))
    # 정류장 개수 N은 한줄의 맨 앞
    N = line[0]
    # 나머지는 각 정류장의 충전 용량 입력이 n-1번 정류장까지만 들어오니까
    # 마지막 정류장을 나타내기 위해서 [0] 추가
    bus_stop = line[1:] + [0]
    # print(N, bus_stop)

    # 우리가 원하는 답 : 최소한의 충전지 교체 횟수
    min_v = 101

    # 1번 정류장(인덱스상으로는 0)에서 출발 // 충전횟수에서는 제외
    backtracking(0, 0)
    print(f'#{tc} {min_v}')