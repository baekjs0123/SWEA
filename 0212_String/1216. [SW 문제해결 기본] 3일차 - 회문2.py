import sys
sys.stdin = open('sample_input.txt', 'r')

def manacher(s):
    """
    Manacher 알고리즘을 이용하여 문자열 s에서 최대 회문(앞뒤로 읽어 동일한 부분 문자열)의 길이를 구합니다.
    전처리: s를 '^#'와 '#$'로 감싸고, 각 문자 사이에 '#'을 삽입하여 홀수/짝수 회문을 통일하여 처리합니다.

    예시: s = "ABBA" 인 경우,
         T = "^#A#B#B#A#$" 가 됩니다.

    P[i]는 전처리된 문자열 T에서 인덱스 i를 중심으로 하는 회문의 반지름(중심 제외 좌우 확장된 길이)을 저장합니다.
    최종적으로 max(P)는 원래 문자열에서의 최대 회문 길이를 의미합니다.
    """
    # 전처리: 문자열 s를 특수문자로 감싸고, 각 문자 사이에 '#'을 삽입합니다.
    T = '^#' + '#'.join(s) + '#$'
    n = len(T)
    P = [0] * n  # 각 인덱스에서의 회문 반지름을 저장할 배열
    center = right = 0  # 현재 회문의 중심(center)과 오른쪽 경계(right)

    # T[0]와 T[n-1]은 경계 문자이므로 1부터 n-2까지 탐색합니다.
    for i in range(1, n - 1):
        # i의 mirror (대칭 위치)는 2*center - i
        mirror = 2 * center - i

        # 만약 i가 현재 팰린드롬의 오른쪽 경계 내에 있다면,
        # 최소한 mirror의 값 또는 (right - i) 만큼은 팰린드롬이 형성됩니다.
        if i < right:
            P[i] = min(right - i, P[mirror])

        # i를 중심으로 팰린드롬을 좌우로 확장합니다.
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # 만약 i + P[i]가 기존의 right보다 더 오른쪽으로 확장되었다면, center와 right를 업데이트합니다.
        if i + P[i] > right:
            center, right = i, i + P[i]

    # P 배열에서 최대값을 구하면 전처리된 문자열 T에서의 최대 회문 반지름입니다.
    # 전처리에서 삽입한 '#'들은 실제 문자 길이에 영향을 주지 않으므로,
    # 최종적으로 max(P)가 원래 문자열에서의 최대 회문 길이가 됩니다.
    return max(P)


# 메인 코드: 10개의 테스트 케이스에 대해 100x100 격자판에서 행과 열 각각의 최대 회문 길이를 구합니다.
for _ in range(10):
    tc = int(input())
    # 100개의 줄을 입력받아 각 줄을 문자 리스트(길이 100)로 저장합니다.
    arr = [list(input().strip()) for _ in range(100)]
    # zip(*)를 사용하여 행렬 전치: 각 열을 튜플 형태로 col_arr에 저장합니다.
    col_arr = list(zip(*arr))

    max_len_overall = 0  # 전체 격자판에서 발견한 최대 회문 길이

    # 각 행과 각 열에 대해 최대 회문 길이를 구합니다.
    for i in range(100):
        # arr[i]는 문자 리스트이므로 ''.join(arr[i])로 문자열로 변환해도 좋습니다.
        row_str = ''.join(arr[i])
        row_max = manacher(row_str)

        # col_arr[i]는 튜플이므로 ''.join(col_arr[i])로 문자열로 변환합니다.
        col_str = ''.join(col_arr[i])
        col_max = manacher(col_str)

        # 두 값과 현재까지의 전체 최대값을 비교하여 갱신합니다.
        max_len_overall = max(max_len_overall, row_max, col_max)

    # 결과 출력: 테스트케이스 번호와 전체 최대 회문 길이를 출력합니다.
    print(f"#{tc} {max_len_overall}")