import sys

sys.stdin = open('sample_input.txt', 'r')

def binary_search(P, target_page):
    # P: 총 페이지 수
    # target_page: 찾고자 하는 페이지 번호
    start = 1
    end = P
    count = 0  # 탐색 횟수

    while start <= end:
        middle = int((start + end) / 2)  # 중간 페이지 계산
        count += 1  # 탐색 횟수 증가
        if middle == target_page:
            return count  # 목표 페이지를 찾으면 탐색 횟수 반환
        elif middle > target_page:
            end = middle  # 중간 페이지보다 목표 페이지가 작으면 왼쪽 영역 탐색
        else:
            start = middle  # 중간 페이지보다 목표 페이지가 크면 오른쪽 영역 탐색

    return count  # 이론상으로는 도달하지 않음

# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    # 총 페이지 수 P, A의 목표 페이지, B의 목표 페이지 입력
    P, A, B = map(int, input().split())

    # A와 B의 탐색 횟수 계산
    countA = binary_search(P, A)
    countB = binary_search(P, B)

    # 결과 비교 및 출력
    if countA < countB:
        result = 'A'
    elif countA > countB:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')
