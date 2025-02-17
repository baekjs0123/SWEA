import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    deck = []
    j = N // 2 + N % 2
    first = card[:j]
    second = card[j:]
    while first or second:
        if first:
            deck.append(first.pop(0))
        if second:
            deck.append(second.pop(0))
    print(f'#{tc}', *deck)

    # deck =  [0] * N
    #
    # ans = ''
    # i = 0               # 먼저 놓는 카드 인덱스
    # j = (N + 1) // 2    # 나중에 놓는 카드 인덱스
    # k = 0               # 셔플덱의 인덱스
    # while k < N:        # 남은 카드가 있으면
    #     if i < (N + 1)//2:
    #         deck[k] = card[i]
    #         i += 1
    #         k += 1
    #     if j < N:
    #         deck[k] = card[j]
    #         j += 1
    #         k += 1
    # print(f'#{tc}', *deck)
