T = 10
for tc in range(1, T + 1):
    dump_cnt = int(input())     # 덤프 횟수
    box_heights = list(map(int, input().split()))   # 박스들의 높이 배열
    '''
    dump_cnt만큼 반복문을 돌면서
    box_heights의 최대값, 최소값을 구하고 최대값 -1 최소값 +1 해준다.
    반목문이 끝났을 때 최대값 - 최소값 을 출력한다. 
    '''
    for i in range(dump_cnt):
        # max_height = max(box_heights)
        # min_height = min(box_heights)
        for j in range(len(box_heights)):
            if box_heights[j] == max(box_heights):
                box_heights[j] -= 1

            if box_heights[j] == min(box_heights):
                box_heights[j] += 1

    print(f'#{tc} {max(box_heights) - min(box_heights)}')
