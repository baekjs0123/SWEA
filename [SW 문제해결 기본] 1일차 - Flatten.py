T = 10
for tc in range(1, T + 1):
    dump_cnt = int(input())     # 덤프 횟수
    box_heights = list(map(int, input().split()))   # 박스들의 높이 배열
    '''
    dump_cnt + 1만큼 반복문을 돌면서
    min_height = box_heights[0]
    max_height = box_heights[0]로 최소 높이, 최대 높이를 구할 준비를 한다.
    이중 for문이 안쪽에서 box_heights의 길이만큼 반복을 돌며 최대 최소값을 구하고 동시에 그 값들의 인덱스 번호도 구한다.
    반복을 다돌고 최대값과 최소값이 나오면 그때 이중 for문의 안쪽에서 구했던 max_idx_num, min_idx_num을 통해 
    box_heights의 최대값 최소값을 1씩 감소시킨다
    반목문이 모두 끝났을 때 최대값 - 최소값 을 출력한다.
    '''
    max_idx_num = 0
    min_idx_num = 0
    for i in range(dump_cnt + 1):
        min_height = box_heights[-1]
        max_height = box_heights[0]

        for j in range(len(box_heights)):
            if max_height <= box_heights[j]:
                max_height = box_heights[j]
                max_idx_num = j
            if min_height >= box_heights[j]:
                min_height = box_heights[j]
                min_idx_num = j
        box_heights[max_idx_num] -= 1
        box_heights[min_idx_num] += 1

    print(f'#{tc} {max_height - min_height}')

    # GPT 풀이법
    # for i in range(dump_cnt):
    #     # 상자의 최대값, 최소값을 담을 변수
    #     min_height = max(box_heights)
    #     max_height = min(box_heights)
    #
    #     # 최대값과 최소값의 인덱스 찾기
    #     max_idx = box_heights.index(max_height)
    #     min_idx = box_heights.index(min_height)
    #
    #     # 최대값과 최소값의 차이가 1 이하이면 평탄화 완료
    #     if max_height - min_height <= 1:
    #         break
    #
    #     # 가장 높은 상자에서 가장 낮은 상자로 상자 이동
    #     box_heights[max_idx] -= 1
    #     box_heights[min_idx] += 1
    # # 최종적으로 최고점과 최저점의 차이 계산
    # final_max = max(box_heights)
    # final_min = min(box_heights)
    # result = final_max - final_min
    #
    # print(f'#{tc} {result}')

