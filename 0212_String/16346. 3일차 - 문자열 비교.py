import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    pattern = input() # 찾아야 할 패턴
    text = input() # 텍스트
    # 패턴의 길이
    pl = len(pattern)

    # 텍스트의 길이
    tl = len(text)

    # 패턴에서 가져올 글자의 위치
    pi = 0
    # 텍스트에서 가져올 글자의 위치
    ti = 0

    # 일단 없다고 생각하고 결과값 설정
    answer = 0
    while ti < tl and pi < pl:
        # 텍스트의 ti 위치에 있는 글자와
        # 패턴의 pi 위치에 있는 글자가 같으면
        # ti += 1, pi += 1
        if pattern[pi] == text[ti]:
            pi += 1
            ti += 1
        # 텍스트의 ti 위치에 있는 글자와
        # 패턴의 pi 위치에 있는 글자가 다르면
        else:

            # 텍스트 비교 시작 위치는 이전 시작 위치 + 1
            # 다음 위치 = 현재 위치 - 비교 횟수 + 1
            ti = ti - pi + 1
            # 패턴 비교 시작 위치는 0으로 되돌리고
            pi = 0
        # 패턴과 텍스트의 글자가 계속 일치해서
        # 일치한 횟수  == 패턴의 길이
        # 패턴을 텍스트 안에서 찾았다!
        if pi == pl:
            answer = 1
            break

    print(f'#{tc} {answer}')


