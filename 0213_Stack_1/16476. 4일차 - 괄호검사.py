import sys

sys.stdin = open('sample_input.txt', 'r')


def check_bracket(s):
    stack = []  # 스택 초기화

    for char in s:
        if char in '({':  # 여는 괄호일 경우
            stack.append(char)  # 스택에 추가
        elif char in '})':  # 닫는 괄호일 경우
            if not stack:  # 스택이 비어있으면
                return 0  # 짝이 맞지 않음
            top = stack.pop()  # 스택의 최상단 요소 제거
            if (char == ')' and top != '(') or (char == '}' and top != '{'):
                return 0  # 짝이 맞지 않음

    if stack:  # 모든 검사가 끝난 후 스택이 비어있지 않으면
        return 0  # 짝이 맞지 않음
    return 1  # 모든 짝이 맞음


T = int(input())
for tc in range(1, T + 1):
    code = input()
    result = check_bracket(code)
    print(f'#{tc} {result}')
