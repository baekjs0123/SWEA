# 승자를 정하는 함수
# i ~ j 번까지 사람 중에서 승자를 정하고 게임 결과 정하기
def tournament(i, j):
    # 분할 단계
    # 쪼갤수 없을때까지 쪼개기
    if i == j:
        # 시작과 끝이 같다 => 사람 1명남음, 쪼개기 불가
        return i
    else:
        # 왼쪽 그룹의 승자 vs 오른쪽 그룹의 승자
        # 왼쪽
        left = tournament(i, (i + j) // 2)
        # 오른쪽
        right = tournament((i + j) // 2 + 1, j)
        # 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자
        if card_arr[left] == card_arr[right]:
            return left if left < right else right
        # 왼쪽: 가위, 오른쪽:바위
        if card_arr[left] == 1 and card_arr[right] == 2:
            return right
        # 왼쪽: 바위, 오른쪽:보
        elif card_arr[left] == 2 and card_arr[right] == 3:
            return right
        # 왼쪽: 보, 오른쪽:가위
        elif card_arr[left] == 3 and card_arr[right] == 1:
            return right
        # 위 경우가 다 아니면 승자 왼쪽
        else:
            return left

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card_arr = list(map(int, input().split()))  # 1: 가위, 2: 바위, 3: 보
    winner = tournament(0, N - 1)
    print(f'#{tc} {winner + 1}')
