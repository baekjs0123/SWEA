import sys
sys.stdin = open('input.txt', 'r')

def max_len_palindrome(row):
    """
    주어진 문자열(row)에서 모든 중심에 대해 회문(앞뒤로 읽어 동일한 문자열)을
    한 번의 반복으로 검사하여 최대 회문 길이를 반환하는 함수입니다.

    아이디어:
      - 문자열의 모든 가능한 '중심'을 고려하면 총 (2*L - 1)개가 있습니다. 100개 기준 199개
        (L은 row의 길이)
      - center가 짝수이면 중심은 한 문자(홀수 길이 회문),
        center가 홀수이면 중심은 두 문자 사이(짝수 길이 회문)로 설정합니다.
      - 각 중심에서 좌우로 확장하면서 문자가 일치하는지 검사하고,
        일치하는 동안 회문의 길이를 갱신합니다.
    """
    L = len(row)  # 문자열의 길이
    max_len = 0  # 현재까지 발견한 최대 회문 길이

    # 0부터 2*L - 2까지 center를 순회 (총 2*L - 1개의 center)
    for center in range(2 * L - 1):
        # 중심을 기준으로 좌측 인덱스는 center//2
        left = center // 2
        # center가 홀수이면, 오른쪽 인덱스는 left + 1, 짝수이면 left와 동일
        right = left + (center % 2)

        # 좌우 인덱스가 범위 내에 있고, 두 문자가 일치하는 동안 확장합니다.
        while left >= 0 and right < L and row[left] == row[right]:
            current_len = right - left + 1  # 현재 회문의 길이 계산
            if current_len > max_len:
                max_len = current_len  # 최대 길이 갱신
            left -= 1  # 왼쪽으로 한 칸 확장
            right += 1  # 오른쪽으로 한 칸 확장

    return max_len

for _ in range(10):
    tc = int(input())
    arr = [list(input().strip()) for _ in range(100)]
    # zip(*)를 사용해 행렬을 전치하여, 각 열을 col_arr에 저장
    col_arr = list(zip(*arr))
    max_len_overall = 0  # 전체 격자판에서 발견한 최대 회문 길이를 저장할 변수
    for i in range(100):
        # i번째 행에서의 최대 회문 길이
        row_max = max_len_palindrome(arr[i])
        col_max = max_len_palindrome(col_arr[i])
        # 두 값과 현재까지의 전체 최대값을 비교하여 갱신
        max_len_overall = max(max_len_overall, row_max, col_max)

    # 결과 출력: 예시 형식에 맞춰 "#테스트케이스번호 최대회문길이" 형태로 출력
    print(f"#{tc} {max_len_overall}")