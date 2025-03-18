# import sys
#
# sys.stdin = open('input.txt', 'r')


def merge_sort(start, end):
    # 1. 종료 조건
    # 더 이상 쪼갤 수 없음?? => 원소가 한개 남았을때
    if start == end - 1:
        # 길이가 1일때의 시작, 끝을 return
        return start, end

    # 2. 재귀 호출
    # 분할 & 정복
    # 절반씩 나누기 (쪼갤수 있으면 계속 반으로 쪼개기)
    mid = (start + end) // 2

    # 1. 왼쪽 부분 정렬하기
    left_s, left_e = merge_sort(start, mid)
    # 2. 오른쪽 부분 정렬하기
    right_s, right_e = merge_sort(mid, end)

    # 병합하여 정렬하기 왼쪽과 오른쪽 중에서 작은거부터 꺼내서 큰 배열 만들기
    # 왼쪽부분, 오른쪽 부분 합친 후에 다시 범위 return
    merge(left_s, left_e, right_s, right_e)

    # start 에서 end까지 정렬 완료
    return start, end


def merge(left_s, left_e, right_s, right_e):
    global cnt

    # 왼쪽배열의 제일 작은 원소의 인덱스 : l
    # 오른쪽 배열의 제일 작은 원소의 인덱스 : r
    l, r = left_s, right_s

    # 왼쪽 마지막 원소의 크기가 오른쪽 마지막 원소보다 크면 개수 + 1
    if arr[left_e-1] > arr[right_e-1]:
        cnt += 1

    # 합쳐서 만들어지는 큰 배열의 길이
    N = right_e - left_s

    # 정렬결과
    result = [0] * N

    # 정렬 결과 배열에 높을 원소의 위치
    idx = 0

    # 정렬 시작(병합 시작)
    # 왼쪽과 오른쪽 부분 중에서 제일 작은거부터 골라서
    # result의 맨 앞에다가 추가

    # 왼쪽 제일 앞에있는 원소가 오른쪽 보다 작으니
    # 왼쪽에 있는 원소를 result에 추가
    # 왼쪽에 원소가 남아있고 and 오른쪽에 원소가 남아있고
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            # 왼쪽 원소 하나 썼으니까 그다음 비교 대상은
            # 왼쪽에서 뒤로 한칸 이동
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            # 오른쪽이 작아서 오른쪽부분의 원소를 result에 추가
            r += 1
            idx += 1

    # 왼쪽이나 오른쪽에 원소가 남아있지 않은경우
    # 왼쪽 원소 x 오른쪽에만 있는경우
    # 오른쪽 부분 남은거 모두 result에 추가
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    # 왼쪽에만 있고 오른쪽 원소 x
    # 왼쪽 부분 남은거 모두 result에 추가
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    # 정렬 결과를 원래 배열에 복사
    for i in range(N):
        arr[left_s + i] = result[i]


T = int(input())

for tc in range(1, T+1):
    # 정렬할 리스트의 길이
    N = int(input())

    # 정렬할 리스트
    arr = list(map(int, input().split()))

    # 합칠때 왼쪽의 마지막 원소가 오른쪽의 마지막 원소보다 큰 경우의 수
    cnt = 0

    # 정렬
    merge_sort(0,N)


    # 답출력
    print(f"#{tc} {arr[N//2]} {cnt}")

