import sys
sys.stdin = open('input.txt', 'r')

# 스택 밖에 있을때 우선순위
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
# 스택 안에 있을때 우선순위
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""
    # 후위표기식을 만들때 사용할 스택
    stack = []

    # 문자열(중위표기식)에서 글자 하나씩 떼어와서 식을 만들자
    for i in range(n):
        # infix[i] : 중위표기식의 i번째 글자
        if infix[i] not in "(+-*/)":
            # i번째 글자가 연산자가 아니다 => 피연산자
            # 피연산자는 그냥 그대로 출력
            postfix += infix[i]
        else:
            # i번째 글자가 연산자다.
            if infix[i] == ")":
                # i번째 글자가 닫는괄호인가?
                # 여는 괄호가 나올때까지 pop 해서 출력
                # () 안의 연산자가 최우선으로 연산되어야 한다.
                # 우선순위가 가장 높음
                # 식에 먼저 써주어야함.

                while stack:
                    # 연산자 하나 꺼내기
                    op = stack.pop()
                    # 꺼냈는데 여는괄호면 꺼내기 중단
                    if op == "(":
                        break

                    # 여는 괄호가 아니다 => 식에 출력
                    postfix += op
            else:
                # i번째 글자가 닫는괄호가 아닌 다른 연산자
                # 현재 연산자(infix[i])의 우선순위 : icp[infix[i]]
                # 스택의 top에 있는 연산자의 우선순위 : isp[stack[-1]]
                # 두개를 비교에서 우선순위가 누가 높은지 판별

                # 1. 현재 연산자의 우선순위보다 스택의 top에 있는 우선순위가
                # 같거나 높으면?? => 스택안에 있는 연산자가 먼저 계산되어야하니까
                # pop 해서 출력
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()

                # 2. 스택의 탑에 있는 연산자의 우선순위가 나보다 작으면 push
                stack.append(infix[i])

    # 스택에 남은 연산자 모두 출력
    while stack:
        postfix += stack.pop()

    return postfix

# 후위표기식을 계산하는 함수
def get_result(postfix):
    # 후위표기식의 계산방법
    # 앞에서부터 쭉 한번씩만 보면된다.
    # 연산자를 만나면 제일 최근에 만난 피연산자 두개 가지고 연산
    # 연산결과를 또 저장해야 다른 연산자의 피연산자로 활용

    stack = []
    for token in postfix:
        # 후위표기식에서 글자 하나씩 떼어오기

        # 떼어온 글자가(토큰)이 피연산자면 스택에 넣기
        if token not in "+-*/":
            stack.append(int(token))  # 타입 조심

        # 떼어온 글자가(토큰)이 연산자이면 연산에 필요한 만큼 스택에서 피연산자 꺼내기
        else:
            right = stack.pop()
            left = stack.pop()

            # 계산 결과
            result = 0

            # 연산자의 종류에 따라 맞게 계산
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left / right

            stack.append(result)

    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = get_postfix(infix, len(infix))
    result = get_result(postfix)
    print(f'#{tc} {result}')
