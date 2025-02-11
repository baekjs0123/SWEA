import sys

sys.stdin = open('input.txt', 'r')

T = 10
# 2차원 배열의 크기 N * N
N = 8
for tc in range(1, T + 1):
    # 우리가 찾아야하는 회문의 길이 M
    M = int(input())

    arr = [input() for _ in range(N)]

    # 회문의 개수 (답)
    count = 0

    # 모든 위치 에서 시작해서 길이가 M인 회문을 만들어봐라
    # 행번호 = i , 열번호 = j
    # 모든 위치(i,j)에서 회문을 만들어본다. 길이 M짜리
    # (i,j) ~ (i,j + M) => 가로 문자열 하나 만들어서 회문인지 판단
    # 행 우선 순회
    for i in range(N):
        # 각 행에서 슬라이딩 윈도우로 부분 문자열 추출
        for j in range(N - M + 1): # 인덱스에러를 방지하기 위해 범위를 N - M + 1로 설정.
            palindrome = arr[i][j: j + M] # 길이가 M인 부분 문자열
            # 회문이면 count 증가
            if palindrome == palindrome[::-1]:
                count += 1
    # (i,j) ~ (i + M,j) => 세로 문자열 하나 만들어서 회문인지 판단
    # 열 우선 순회
    for j in range(N):
        palindrome = []
        for i in range(N - M + 1):
            # 리스트 컴프리헨션을 이용해 세로로 길이 M인 문자열 생성
            palindrome = ''.join(arr[i + k][j] for k in range(M))
            if palindrome == palindrome[::-1]:
                count += 1
    print(f'#{tc} {count}')
