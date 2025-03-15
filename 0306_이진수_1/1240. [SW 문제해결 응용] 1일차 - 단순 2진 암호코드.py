# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]
    decoding_dic = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5',
                    '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
    decoding = ''
    result = 0
    for i in range(N):
        if '1' in password[i]:
            for j in range(M - 1, -1, -1):
                if password[i][j] == '1':
                    for k in range(j, -1, -7):
                        temp = password[i][k - 6:k + 1]
                        decoding = decoding_dic.get(temp, '') + decoding
                if len(decoding) == 8:
                    break
    odd = 0
    even = 0

    for i in range(len(decoding)):
        if i % 2:
            even += int(decoding[i])
        else:
            odd += int(decoding[i])
    if ((odd * 3) + even) % 10 == 0:
        result = odd + even

    print(f'#{tc} {result}')