T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    '''
    1<=T<=50, 10 <= N <= 100
    이중배열을 완전 탐색하면서 배열의 요소가 1인 경우 요소가 0이 나올때 까지 탐색하며 가로의 길이를 측정한다.
    세로길이 역시 동일한 방법으로 세로의 길이를 측정한다.
    가로 * 세로의 넓이를 구하고 이 넓이가 최대값여부인지 확인하고 최대값을 출력한다.
    '''
    max_area = 0    # 사각형 넓이 최대값을 담을 변수
    for r in range(N):
        for c in range(N):
            height = 0  # 세로크기를 담을 변수, 아래에서 1부터 0이 나올때까지 길이를 측정한 후 넓이를 계산하고 넘어오면 다시 0으로 초기화시켜준다.
            width = 0   # 가로 크기를 담을 변수, 아래에서 1부터 0이 나올때까지 길이를 측정한 후 넓이를 계산하고 넘어오면 다시 0으로 초기화시켜준다.
            if arr[r][c] == 1:
                for i in range(r, N):
                    if arr[i][c]:
                        height += 1
                    else:
                        break
                for j in range(c, N):
                    if arr[r][j]:
                        width += 1
                    else:
                        break
                area = width * height
                if max_area < area:
                    max_area = area
    print(f'#{tc} {max_area}')