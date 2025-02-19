import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    # 원형큐
    num_arr = list(map(int, input().split()))
    qsize = 9

    # 원형 큐 생성
    cq = [0] * qsize
    front = rear = 0
    # 입력 데이터를 큐에 저장 (8개 숫자)
    for i in range(8):
        rear = (rear + 1) % qsize
        cq[rear] = num_arr[i]
    # 1부터 5까지 순환할 감소값
    decrement = 1
    while True:
        front = (front + 1) % qsize
        # 감소값을 적용하여 새 값을 계산
        item = cq[front] - decrement

        # 계산된 값이 0 이하라면 암호 생성 종료
        if item <= 0:
            item = 0
            rear = (rear + 1) % qsize
            cq[rear] = item
            break
        else:
            rear = (rear + 1) % qsize
            cq[rear] = item
        # 감소값을 1부터 5까지 순환
        decrement = decrement + 1 if decrement < 5 else 1

    # 최종 암호는 front 위치의 다음 요소부터 8개 숫자 (원형 큐 순서를 맞추기 위해)
    result = []
    for i in range(8):
        index = (front + 1 + i) % qsize
        result.append(cq[index])
    print(f'#{tc}', *result)

