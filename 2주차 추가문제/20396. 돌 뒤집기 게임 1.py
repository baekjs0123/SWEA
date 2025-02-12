# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N : 돌의 갯수, M: 돌 뒤집을 횟수
    N, M = map(int, input().split())
    rock_status = list(map(int, input().split())) # 초기 돌의 상태
    for _ in range(M):
        i, j = map(int, input().split())    # i: i번째 돌(인덱스로 접근하려면 i - 1로 접근해야함) j: i ~ j개의 돌을 뒤집어야함
        # i번째 돌의 모양으로 i ~ j번째 까지 만들기 위한 변수
        rock_change = rock_status[i - 1]
        # 반복문을 딱 j개 만큼 돌리기 위해 마지막 인덱스 계산
        last_idx = i + j - 1
        # 만약 last_idx가 rock_status의 범위를 벗어날 경우 인덱스에러를 막기 위해 last_idx를 N으로 설정
        if last_idx > N:
            last_idx = N
        # i부터 ~ j개 까지 i번째의 돌모양으로 변경
        for k in range(i - 1, last_idx):
            rock_status[k] = rock_change

    print(f'#{tc} {" ".join(map(str, rock_status))}')
