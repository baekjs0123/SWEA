import sys
sys.stdin = open('input.txt', 'r')


def dfs(swap_cnt):
    global max_result
    # 입력받은 수 만큼 swap 했다면 종료
    if swap_cnt == total_swap_cnt:
        # 최대 상금 초기화
        # [주의사항] number = 문자열 리스트
        #   => 숫자로 만들어 주어야 한다.
        max_result = max(max_result, int(''.join(number)))
        return

    # 모든 케이스를 swap 하도록 구현
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            # 재귀호출 전 : swap 을 한다
            number[i], number[j] = number[j], number[i]

            #   사용하지 않은 수라면
            #   사용했다고 체크하고
            # 재귀호출 : swap 한 번 했다고 전달

            str_number = ''.join(number)
            if visited.get((swap_cnt, str_number)) is None:
                visited[(swap_cnt, str_number)] = 1
                dfs(swap_cnt + 1)

            # 돌아왔을 때 : swap 한 수를 원래대로 돌려준다.
            number[i], number[j] = number[j], number[i]


T = int(input())
for tc in range(1, T + 1):
    # number는 int가 아니라, 리스트로 입력 받아야 swap이 편하다.
    number, total_swap_cnt = input().split()
    number = list(number)
    total_swap_cnt = int(total_swap_cnt)
    max_result = -1  # 최대 상금
    # 딕셔너리는 내부적으로 "해시함수"라는 것을 통해 해시값으로 키를 변환해서 저장하고 있음
    # -> 리스트는 해시값으로 변환할 수 가 없어서 키 값으로 사용 불가능하다.
    visited = {}  # (몇 번 swap만에, 무슨 숫자가 들어왔다)
    dfs(0)
    print(f'#{tc} {max_result}')