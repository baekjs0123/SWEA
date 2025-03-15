import sys
sys.stdin = open('input.txt', 'r')

def recur(cnt, total_height):
    global  answer
    if total_height >= B:
        answer = min (answer, total_height)
        return

    if cnt == N:
        return

    recur(cnt + 1, total_height + Hi[cnt])
    recur(cnt + 1, total_height)



T = int(input())
for tc in range(1, T + 1):
    # N: 점원 수, B: 선반의 높이
    N, B = map(int, input().split())
    Hi = list(map(int, input().split())) # 점원들 키 리스트
    answer = int(21e8)
    '''
    점원들의 키의 합을 부분집합으로 계산하고 그 중 선반의 높이인 B이상인것들만 모아서
    그 중에 최소값을 찾아서 최소값 - B를 출력한다.
    '''
    recur(0,0)
    print(f'#{tc} {answer - B}')
