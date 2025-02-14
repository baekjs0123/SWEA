import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    '''
    접근법
    Ai와 Bi를 인덱스로 비교해서 값이 다를 때, 해당 인덱스를 기억하고,
    해당 인덱스로부터 N번까지 모두 스위치값을 바꿔준다. 그리고 count +=1 을 한다.
    그리고 최초로 변경했던 인덱스 i값의 다음 인덱스인 i + 1부터 다시
    위 과정을 반복한다. 
    '''
    i = 0
    differnt_idx = 0
    cnt = 0
    while i < N:
        # 스위치를 변경해야하는 시점 = Ai[i] != Bi[i]
        if Ai[i] != Bi[i]:
            #스위치 변경을 시작하는 인덱스 기록
            differnt_idx = i
            # i ~ N까지 스위치 변경
            for i in range(i, N):
                # Ai[i] != 0이면 True, 0이면 False
                if Ai[i]:
                    Ai[i] = 0
                else:
                    Ai[i] = 1
            cnt += 1
            # 새로 스위치 변경을 시작할 인덱스 위치
            i = differnt_idx + 1
        # Ai[i] == Bi[i]일때 i += 1
        else:
            i += 1

    print(f'#{tc} {cnt}')



