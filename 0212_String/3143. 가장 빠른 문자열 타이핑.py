# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    A, B = map(str, input().split())    # A: 텍스트, B: 패턴
    min_v = len(A)
    Ai = 0
    Bi = 0
    Al = len(A)
    Bl = len(B)
    cnt = 0
    while Ai < Al and Bi < Bl:
        if A[Ai] == B[Bi]:
            Bi += 1
            Ai += 1
        else:
            Ai = Ai - Bi + 1
            Bi = 0
        if Bi == Bl:
            cnt += 1
            Bi = 0
    min_v = Al - (Bl - 1) * cnt
    print(f'#{tc} {min_v}')
