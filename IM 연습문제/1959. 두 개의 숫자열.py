import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split()) # N: Ai의 숫자 갯수, M: Bj의 숫자 갯수
    Ai = list(map(int, input().split())) # Ai: N개의 숫자열
    Bj = list(map(int, input().split())) # Bj: M개의 숫자열
    '''
    접근법
    Ai와 Bj 중 더 큰쪽의 배열을 기준으로 잡고 작은쪽을 슬라이딩 윈도우 기법으로 돌린다.
    돌면서 마주보는 값들의 곱들을 모두 더한 뒤 최대값을 구한다. 
    '''
    # Ai와 Bj의 길이비교를 통해 어느쪽이 긴 배열인지 확인하고 저장한다.
    if len(Ai) < len(Bj):
        long_arr = Bj
        short_arr = Ai
    else:
        long_arr = Ai
        short_arr = Bj
    # 최대값을 담을 변수
    max_total_num = 0
    # 큰배열의 길이 - 짧은 배열의 길이만큼 반복문을 돈다
    for i in range(len(long_arr) - len(short_arr) + 1):
        # 반복을 돌때 마다 마주보는 수와의 곱의 합을 담을 변수
        total = 0
        # 작은 배열의 길이 만큼 돌며 마주보는 수와 곱한다
        for j in range(len(short_arr)):
            total += short_arr[j] * long_arr[i + j]
        # max_total_num 과 total을 비교하여 total이 더 크다면
        # max_total_num 을 total로 재할당한다.
        if max_total_num < total:
            max_total_num = total
    print(f'#{t} {max_total_num}')