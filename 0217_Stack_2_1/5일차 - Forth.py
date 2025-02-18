def get_result(postfix):
    stack = []  # 스택 초기화
    tokens = postfix.split()  # 입력 문자열을 공백으로 분리하여 토큰화

    for token in tokens:
        if token.isdigit():  # 토큰이 숫자인 경우
            stack.append(int(token))  # 스택에 정수로 변환하여 추가
        elif token in ['+', '-', '*', '/']:  # 토큰이 연산자인 경우
            if len(stack) < 2:  # 스택에 피연산자가 두 개 미만인 경우
                return 'error'  # 에러 반환
            b = stack.pop()  # 두 번째 피연산자
            a = stack.pop()  # 첫 번째 피연산자
            if token == '+':
                stack.append(a + b)  # 덧셈 결과를 스택에 추가
            elif token == '-':
                stack.append(a - b)  # 뺄셈 결과를 스택에 추가
            elif token == '*':
                stack.append(a * b)  # 곱셈 결과를 스택에 추가
            elif token == '/':
                if b == 0:  # 0으로 나누는 경우
                    return 'error'  # 에러 반환
                stack.append(a // b)  # 정수 나눗셈 결과를 스택에 추가
        elif token == '.':  # 출력 명령인 경우
            if len(stack) != 1:  # 스택에 값이 하나가 아닌 경우
                return 'error'  # 에러 반환
            return stack.pop()  # 스택의 최종 결과 반환
        else:  # 알 수 없는 토큰인 경우
            return 'error'  # 에러 반환

    return 'error'  # 최종적으로 스택에 값이 남아있지 않은 경우 에러 반환

T = int(input())
for tc in range(1, T + 1):
    postfix = input()
    result = get_result(postfix)
    print(f'#{tc} {result}')