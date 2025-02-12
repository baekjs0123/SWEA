import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    rock_status = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        # i: i번째 돌, j: i번째 돌을 사이에 두고 마주보는 j개의 돌(i - j), (i + j)개까지

        for k in range(j):
            left_idx = (i - 1) + (-k - 1)
            right_idx = (i - 1) + (k + 1)
            if left_idx < 0 or right_idx > N - 1:
                break
            elif rock_status[left_idx] == rock_status[right_idx]:
                if rock_status[left_idx] == 0:
                    rock_status[left_idx] = 1
                    rock_status[right_idx] = 1
                else:
                    rock_status[left_idx] = 0
                    rock_status[right_idx] = 0

    print(f'#{tc} {" ".join(map(str, rock_status))}')