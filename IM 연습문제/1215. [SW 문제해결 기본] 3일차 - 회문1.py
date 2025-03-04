for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    # print(arr)

    cnt = 0
    # 행 우선 순회
    for i in range(8):
        for j in range(8 - N + 1):
            palindrome = arr[i][j: j + N]
            if palindrome == palindrome[::-1]:
                cnt += 1

    # 열 우선 순회
    for j in range(8):
        palindrome = []
        for i in range(8 - N + 1):
            palindrome = ''.join(arr[i + k][j] for k in range(N))
            if palindrome == palindrome[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')


