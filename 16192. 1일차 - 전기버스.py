def drive(K, N):
    # 버스를 운행하는 함수
    # return 0 : 충전소가 제대로 배치되어 있지 않다
    # return 값 > 0 : 충전소가 제대로 배치되어 있다.

    count = 0   # 지금까지 충전한 횟수
    current = K     # 버스가 한번 충전해서 최대로 이동한 상태
    last = 0    # 마지막으로 충전한 위치

    # 종점에 도착하기 전까지는 버스가 계속 이동
    while current < N:
        # 현재 정류장에 충전기가 있나 없나 검사
        # 충전기가 만약 없다면 충전기를 찾아서 다시 뒤로 한칸씩 이동
        # 충전기를 찾을 때 까지
        while stop[current] == 0:
            # current 정류장에 충전기가 없다면 뒤로 한칸 이동
            current -= 1 # 한칸 씩 뒤로 이동
            # 마지막으로 충전한 정류소 까지 와버리면
            # 끝까지 갈 수 있는 방법이 없다.
            if current == last:
                return 0    # 운행불가, 함수 종료
        # 만약 반복문이 중단되서 코드가 여기까지 실행된다면
        # 충전기가 있는 정류소에 도착했다.
        # 마지막으로 충전한 정류소 번호 기억
        last = current
        # 다음 위치로 이동
        current += K
        # 충전 횟수 + 1
        count += 1
    # 만약 반복문이 정상적으로 종료되서 코드가 여기까지 실행된다면
    # 무사히 마지막 정류장까지 도착 할 수 있었다,
    # 충전 횟수 return
    return count




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N = 종점 번호
    # M = 충전기가 설치된 정류장 갯수
    charge_stop_arr = list(map(int, input().split()))   # arr = 충전기가 설치된 정류장의 번호가 담긴 배열
    # 충전이 가능한 정류장인가? 불가능한 정류장인가?
    stop = [0] * N
    # stop[i] == 1: i번 정류장에는 충전기가 있다!
    # stop[i] == 0: i번 정류장에는 충전기가 없다!
    # if stop[i] == 1:
    #   충전해라.
    for i in charge_stop_arr:
        stop[i] = 1
    answer = drive(K, N)
    print(f'#{test_case} {answer}')
    '''
    A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
    
    버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
    
    충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
    
    만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
    '''
    '''
    충전기 M개의 숫자만큼 반복을 돌면서 몇번 정류장에 충전기가 있는 지 확인.
    충전기가 설치 된 정류장에는 1 값을 넣어준다.
    버스가 0번부터 이동하면서 bus + K까지의 거리에 충전소가 2개 이상이라면 마지막 충전소에 멈춰서 충전한다.
    이때 bus에 충전한 정류장 번호를 담는다. 다시 bus + K까지의 거리에 충전소를 탐색. 만약 충전소가 1개라면 해당 충전소에 멈춘다.
    멈출 때마다 count += 1한다. 만약 K까지의 거리 안네 충전소가 하나도 없다면 count = 0을 출력한다.
    '''
    # charge_stop = [0] * (N + 1)     # 충전기가 설치된 정류장
    # count = 0                       # 총 충전 횟수
    # bus = 0                         # 버스의 위치 인덱스
    # charge_count = 0                # 충전소 갯수
    # for charge_num in charge_stop_arr:
    #     for j in range(len(charge_stop)):
    #         if j == charge_num:
    #             charge_stop[j] = 1
    # print(charge_stop)
    #
    # for i in range(len(charge_stop)):
    #     if i <= bus + K:
    #         charge_count += charge_stop[i]



