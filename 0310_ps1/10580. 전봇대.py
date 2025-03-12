# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    wires = []      # 기존 선 저장할 리스트
    answer_cnt = 0  # 교차점 수

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존 선들과 비교
        for prev_start, prev_end in wires:
            # 교차점 조건1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
            if start > prev_start and end < prev_end:
                answer_cnt += 1

            # 교차점 조건2. 기존의 전선보다 시작점이 낮고, 도착점이 높다
            if start < prev_start and end > prev_end:
                answer_cnt += 1
        # 목록에 전선을 추가
        wires.append((start, end))

    print(f'#{tc} {answer_cnt}')


