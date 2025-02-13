import sys
sys.stdin = open('sample_input.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N, s = map(str, input().split())
    s = list(s)
    i = 0
    end = len(s)
    while i < end - 1:

        if s[i] == s[i + 1]:
            s.pop(i)
            s.pop(i)
            end -= 2
            i -= 1
        else:
            i += 1
    print(f'#{tc} {"".join(s)}')

