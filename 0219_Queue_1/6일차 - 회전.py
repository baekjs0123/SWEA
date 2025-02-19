# T = int(input())
# for tc in range(1, T + 1):
#     # N : 숫자 갯수
#     # M : 맨 앞의 숫자를 맨뒤로 보내는 일을 M번 해야함. 작업횟수
#     N, M = map(int, input().split())
#
#     # 입력으로 들어온 한줄 자체를 큐로 사용해버린다.
#     Q = list(map(int, input().split())) + ([0] * M)
#     # Q = [0] * 100000
#
#     front = -1
#     rear = N - 1
#
#     # 원소를 꺼내고 넣는 일을 M번 반복한다.
#     for _ in range(M):
#         # 원소를 꺼내고
#         front += 1
#         item = Q[front]
#
#         # 원소를 넣고
#         rear += 1
#         Q[rear] = item
#
#     # 맨 앞에 있는 원소는? dequeue 연산 한번 더 하면 된다.
#     front += 1
#     item = Q[front]
#
#     print(f'#{tc} {item}')

def is_full():
    return (rear + 1) % N == front

T = int(input())
for tc in range(1, T + 1):
    # N : 숫자 갯수
    # M : 맨 앞의 숫자를 맨뒤로 보내는 일을 M번 해야함. 작업횟수
    N, M = map(int, input().split())

    # 입력으로 들어온 한줄 자체를 큐로 사용해버린다.
    cQ = [0] + list(map(int, input().split()))

    # 원형 큐
    front = 0
    rear = N

    # 원소를 꺼내고 넣는 일을 M번 반복한다.
    for _ in range(M):
        if not is_full():
            # 원소를 꺼내고
            front = (front + 1) % N

            # 원소를 넣고
            rear = (rear + 1) % N

    # 맨 앞에 있는 원소는? dequeue 연산 한번 더 하면 된다.
    front = (front + 1) % N
    item = cQ[front]

    print(f'#{tc} {item}')


