import sys

sys.stdin = open('sample_input.txt', 'r')


def remove_duplicates(s):
    stack = []  # 스택 초기화
    top = -1
    for char in s:
        if stack and stack[top] == char:
            stack.pop()  # 현재 문자와 스택의 top이 같으면 제거
        else:
            stack.append(char)  # 그렇지 않으면 스택에 추가


    return len(stack)  # 최종 스택의 길이 반환


T = int(input())
for tc in range(1, T + 1):
    s = input()
    result = remove_duplicates(s)

    print(f"#{tc} {result}")
