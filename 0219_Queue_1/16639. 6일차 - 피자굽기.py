T = int(input())
for tc in range(1, T + 1):
    # N: 화덕의 크기
    # M: 피자의 개수
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    # 화덕의 크기 + 1만큼의 원형 큐(front 위한 빈칸 1개)
    qsize = N + 1
    # 화덕 역할을 할 원형 큐
    oven = [0] * qsize
    front = rear = 0

    # 화덕에 넣을 수 있을만큼만 피자를 꺼내서 넣는다.
    for i in range(N):
        rear = (rear + 1) % qsize
        oven[rear] = i  # 넣을 때 인덱스랑 맞춰 주거나 최종 답을 구할 때 맞추거나

    # 다음 차례에 화덕에 들어갈 피자 번호 기억
    next_p = N

    # 화덕에서 피자 꺼내서
    # 치즈 반으로 나누고
    # 치즈 아직 남아있으면 다시 넣고
    # 남은 치즈 없으면 빼고
    # 계속 반복

    # 큐가 빌때까지 반복해라
    # 화덕에 피자가 있으면 위의 작업을 계속 반복
    while front != rear: # 화덕이 비어있지 않으면 계속 반복해라
        # 화덕에서 피자를 꺼낸다.
        front = (front + 1) % qsize
        now_p = oven[front]

        # 치즈를 반으로 나눈다
        pizza[now_p] //= 2

        if pizza[now_p] > 0:
            # 다시 넣어라
            rear = (rear + 1) % qsize
            # 아직 치즈 남았으니 다시 넣어
            oven[rear] = now_p
        # 치즈가 모두 녹았다.
        else:
            # 피자를 꺼낸다.
            # 다음에 넣을 피자가 남아있을 경우
            if next_p < M:
                rear = (rear + 1) % qsize
                oven[rear] = next_p
                # 그 다음 피자 번호 기억
                next_p += 1
            # 남아있지 않은 경우
            # 꺼낸 피자가 마지막 피자!!
            # 현재 피자 번호가 now_p니까
            # 마지막 피자 번호가 now_p가 된다.
    print(f'#{tc} {now_p + 1}')