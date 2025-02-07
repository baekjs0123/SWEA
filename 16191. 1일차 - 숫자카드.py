T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # arr = list(map(int, input().split())) # arr에 값이 하나만 담기는 문제 발생
    # 원인: arr를 입력 받을 때  4 9 6 7 9 와 같은 방식이 아니고 49679와 같이 입력 받고 있어서
    # 공백이 없기때문에 split()못함. 위 코드와 같이 동작하면 arr에 담기는 값은 [49679가 되어버림]
    arr = list(map(int, input()))

    # 0 ~ arr의 가장 큰수 + 1만큼 counts 배열 생성
    counts = [0] * (max(arr) + 1)

    temp = [0] * N
    # max_card_num = 가장 많은 카드에 적힌 숫자를 담을 변수
    max_card_num = 0
    # max_card_num_cnt = 가장 많은 카드에 적힌 숫자가 몇 장인지를 담을 변수
    max_card_num_cnt = 0
    # 카드 장수  N만큼 반복을 돌며 카운트 시작
    for i in range(N):
        counts[arr[i]] += 1
    # 0 ~ counts의 크기 만큼 반복문
    for i in range(len(counts)):
        if max_card_num_cnt <= counts[i]: # max_card_num_cnt가 counts[i]보다 작거나 같을 때
            max_card_num_cnt = counts[i]
            max_card_num = i
    print(f'#{test_case} {max_card_num} {max_card_num_cnt}')
