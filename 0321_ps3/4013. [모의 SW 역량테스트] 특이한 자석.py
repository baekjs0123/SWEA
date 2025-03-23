import sys

sys.stdin = open('input.txt', 'r')
'''
1. 빨간색 화살표 위치가 0번째 인덱스이다. 따라서 자석이 서로 붙어있는 날의 인덱스번호는
2가 오른쪽, 왼쪽은 6번 인덱스이다.

2. 자석의 회전방향을 저장할 rotations 리스트를 만들고 매번 자석의 회전방향을 저장해준다. 

3. 만약 있는 자석중에 회전하지 않는 자석이 있다면 그 뒤에 모든 자석은 회전하지 않는다.

4. 모든 회전이 끝난 후 gears[i][0] 이 N극이면 0점, S극이면 각 ¡자석마다 1, 2, 4, 8점을 획득한다.
2의 i제곱을 하면 1,2,4,8점씩 더해줄 수 있다.
'''
T = int(input())

for tc in range(1, T + 1):
    # 자석을 회전시키는 횟수 K를 입력받습니다.
    K = int(input())

    # 4개의 자석에 대한 극 정보 (각 자석은 8개의 숫자로 구성)
    gears = [list(map(int, input().split())) for _ in range(4)]

    # K 번의 회전 명령을 처리합니다.
    for _ in range(K):
        # 회전 명령: 자석 번호와 회전 방향을 입력받습니다.
        num, direction = map(int, input().split())
        num -= 1  # 자석 번호를 0번 인덱스에 맞게 조정

        # 각 자석의 회전 방향을 저장하는 배열 (0이면 회전 없음)
        rotations = [0] * 4
        rotations[num] = direction  # 선택한 자석은 주어진 방향으로 회전

        # 선택한 자석의 왼쪽으로 회전 전파
        for i in range(num - 1, -1, -1):
            # i번 자석의 오른쪽 날(인덱스 2)와 i+1번 자석의 왼쪽 날(인덱스 6)을 비교
            if gears[i][2] != gears[i + 1][6]:
                rotations[i] = -rotations[i + 1]
            else:
                break  # 같은 극이면 전파 중단

        # 선택한 자석의 오른쪽으로 회전 전파
        for i in range(num + 1, 4):
            # i-1번 자석의 오른쪽 날(인덱스 2)와 i번 자석의 왼쪽 날(인덱스 6)을 비교
            if gears[i - 1][2] != gears[i][6]:
                rotations[i] = -rotations[i - 1]
            else:
                break  # 같은 극이면 전파 중단

        # 저장된 회전 방향에 따라 각 자석 회전 적용
        for i in range(4):
            if rotations[i] == 1:  # 시계방향 회전
                gears[i] = [gears[i][-1]] + gears[i][:-1]
            elif rotations[i] == -1:  # 반시계방향 회전
                gears[i] = gears[i][1:] + [gears[i][0]]

    # 모든 회전 후 최종 점수 계산
    score = 0
    for i in range(4):
        if gears[i][0] == 1:  # 0번 인덱스가 S극(1)인 경우
            score += (2 ** i)  # 2**i 점을 획득 (자석 순서에 따라 1, 2, 4, 8 점)

    print(f"#{tc} {score}")