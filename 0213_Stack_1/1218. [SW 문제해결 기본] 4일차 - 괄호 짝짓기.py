import sys
sys.stdin = open('sample_input.txt', 'r')

def is_valid(c, top):
    return (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '[') or (c == '>' and top != '<')

def check_bracket(s):
    stack = []
    for c in s:
        if c in '({[<':
            stack.append(c)
        elif c in '>]})':
            if not stack:
                return 0
            top = stack.pop()
            if is_valid(c, top):
                return 0
    if stack:
        return 0
    return 1

for tc in range(1, 11):
    s_len = int(input())
    s = list(input())
    result = check_bracket(s)
    print(f'#{tc} {result}')
