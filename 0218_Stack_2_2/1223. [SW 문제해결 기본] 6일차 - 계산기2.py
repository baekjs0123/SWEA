icp = {"+": 1, "*": 2}
# 스택 안에 있을때 우선순위
isp = {"+": 1, "*": 2}

for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''
    stack = []
    for i in range(N):
        if infix[i] not in '(+*)':
            postfix += infix[i]
        else:
            if infix[i] == ')':
                while stack:
                    op = stack.pop()
                    if op == '(':
                        break

                    postfix += op
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    # print(postfix)
    stack = []
    for token in postfix:
        if token not in '+*':
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            result = 0

            if token == '+':
                result = left + right
            elif token == '*':
                result = left * right

            stack.append(result)
    result = stack.pop()
    print(f'#{tc} {result}')