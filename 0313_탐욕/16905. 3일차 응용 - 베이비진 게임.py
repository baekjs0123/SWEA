import sys

sys.stdin = open('input.txt', 'r')


def greedy(deck, player):
    global winner
    # 카운트 세기
    cnt_arr = [0] * 10

    for i in deck:
        cnt_arr[i] += 1
    # 카운트를 통해 run or triplet 판단
    for i in range(len(cnt_arr)):
        if cnt_arr[i] >= 3:
            winner = player
            return
        if i + 2 < len(cnt_arr) and cnt_arr[i] >= 1 and cnt_arr[i + 1] >= 1 and cnt_arr[i + 2] >= 1:
            winner = player
            return
    return


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    turn = 0

    player1 = []  # 1번 플레이어 카드 덱
    player2 = []  # 2번 플레이어 카드 덱

    # -1 : 아직 승자는 정해지지 않음
    # 0 : 무승부
    # 1 : 1번승
    # 2 : 2번승
    winner = -1

    # 6개의 카드를 골라야 하므로 턴은 최대 6번 진행
    while turn < 6:
        # 카드 잘 나눠서 분배
        player1.append(cards[turn * 2])
        player2.append(cards[turn * 2 + 1])

        # run 또는 triplet을 확인하려면 최소 카드 3장 필요
        if turn >= 3:
            # 1번 플레이어 순열 or 탐욕 방법 사용해서 승자 판단
            greedy(player1, 1)
            if winner != -1:  # 승자가 정해졌으면 더 하면 안돼
                break

            # 2번 플레이어 순열 or 탐욕 방법 사용해서 승자 판단
            greedy(player2, 2)
            if winner != -1:  # 승자가 정해졌으면 더 하면 안돼
                break

        # 턴 증가
        turn += 1

    # 카드 다 나눠서 판단했는데 승자가 없는 경우는 무승부
    if winner == -1:
        winner = 0

    print(f"#{tc} {winner}")