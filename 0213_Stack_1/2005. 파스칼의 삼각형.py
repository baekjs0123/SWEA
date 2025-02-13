import sys
sys.stdin = open('sample_input.txt', 'r')


def pascal(i, j):
    # i: 행 번호
    # j: 열번호, 해당 행에서의 위치
    # 각 행의 처음과 끝은 항상 1
    if j == 0 or j == i:
        return 1
    # 재귀 호출: 현재 요소는 이전 행의 왼쪽 요소와 오른쪽 요소의 합
    return pascal(i - 1, j - 1) + pascal(i - 1, j)
    '''
    위 재귀 함수의 동작 원리 설명
    예시로 pascal(3, 1) 인 경우:

    pascal(3, 1):

    j가 0이나 3이 아니므로 재귀 함수 호출
    계산식: pascal(2, 0) + pascal(2, 1)
    
    pascal(2, 0):
    여기서는 j == 0이므로 바로 1을 반환.
    
    pascal(2, 1):
    역시 if 조건에 해당하지 않으므로,
    계산식: pascal(1, 0) + pascal(1, 1)
    
    pascal(1, 0):
    j == 0이므로 1 반환
    pascal(1, 1):
    j == i (1 == 1)이므로 1 반환
    **pascal(2, 1)**는 1 + 1 = 2.
    
    최종적으로 **pascal(3, 1)**은 pascal(2, 0) = 1과 pascal(2, 1) = 2
    1 + 2 = 3이라는 값이 나옴.
    '''



# 테스트 케이스의 개수를 입력받음
T = int(input())

for tc in range(1, T + 1):
    # N : 삼각형의 크기
    N = int(input())
    print(f"#{tc}")

    for i in range(N):
        row_numbers = []
        for j in range(i + 1):
            # 해당 행의 각 숫자를 재귀함수를 통해 계산하여 문자열 리스트에 저장
            row_numbers.append(pascal(i, j))
        print(*row_numbers)
        # print(" ".join(map(str,row_numbers)))
        # 리스트를  map을 활용해서 str로 변환한 후
        # join()으로도 출력가능
