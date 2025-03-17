# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    answer = ''
    while N > 0:
        N *= 2
        if N >= 1:
            N -= 1
            answer += '1'
        else:
            answer += '0'
        if len(answer) >= 13:
            answer = 'overflow'
            break
    print(f'#{tc} {answer}')