import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N: 카드의 개수
    N = int(input())
    # 카드 덱(문자열 리스트)을 입력받음
    deck = input().split()

    # N이 짝수인 경우와 홀수인 경우에 따라 덱을 두 부분으로 나눔
    if N % 2 == 0:
        # 짝수인 경우, 두 절반의 길이가 동일함
        half_deck1 = deck[:N // 2]
        half_deck2 = deck[N // 2:]
    else:
        # 홀수인 경우, 앞쪽(첫 번째) 절반이 한 장 더 많음
        half_deck1 = deck[:(N // 2 + 1)]
        half_deck2 = deck[(N // 2 + 1):]

    new_deck = []
    # 두 덱의 공통된 인덱스 범위까지 교대로 추가
    for i in range(len(half_deck2)):
        new_deck.append(half_deck1[i])
        new_deck.append(half_deck2[i])
    # 홀수인 경우, 첫 번째 덱에 남은 마지막 카드를 추가
    if len(half_deck1) > len(half_deck2):
        new_deck.append(half_deck1[-1])

    # 출력 형식에 맞춰 결과 출력
    print(f"#{tc} {' '.join(new_deck)}")
