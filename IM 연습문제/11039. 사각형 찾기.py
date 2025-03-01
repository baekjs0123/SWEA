import pprint

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pprint.pprint(arr)
    '''
    1<=T<=50, 10 <= N <= 100
    이중배열을 완전 탐색하면서 배열의 요소가 1인 경우 요소가 0이 나올때 까지 델타탐색하며 가로의 최대길이를 측정한다.
    세로길이 역시 동일한 방법으로 세로의 최대길이를 측정한다.
    가로 * 세로의 넓이를 구하고 이 넓이가 최대값여부인지 확인하고 최대값을 출력한다.      
    '''
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                nr = r + 1
                nc = c + 1
