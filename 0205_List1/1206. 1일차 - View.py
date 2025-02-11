for test_case in range(1, 10 + 1):
    N = int(input())
    height_lst = list(map(int, input().split()))
    # 전망좋은 집 수를 더할 변수
    viewgood = 0
    for i in range(2, N - 2):
        rmin_view = 0
        lmin_view = 0
        # 건물 오른쪽 조망이 확보된 경우
        right_viewgood = height_lst[i] - height_lst[i + 1] > 0 and height_lst[i] - height_lst[i + 2] > 0
        # print(f'right_viewgood: {right_viewgood}')

        # 건물 왼쪽 조망이 확보된 경우
        left_viewgood = height_lst[i] - height_lst[i - 1] > 0 and height_lst[i] - height_lst[i - 2] > 0
        # print(f'left_viewgood: {left_viewgood}')
        if right_viewgood and left_viewgood:
            # rv1 = 오른쪽 한칸 옆 빌딩과의 높이 차이
            rv1 = height_lst[i] - height_lst[i + 1]
            # rv2 = 오른쪽 두칸 옆 빌딩과의 높이 차이
            rv2 = height_lst[i] - height_lst[i + 2]
            # lv1 = 왼쪽 한칸 옆 빌딩과의 높이 차이
            lv1 = height_lst[i] - height_lst[i - 1]
            # lv2 = 왼쪽 두칸 옆 빌딩과의 높이 차이
            lv2 = height_lst[i] - height_lst[i - 2]

            # 각 rv와 lv를 비교하여 작은 값을 각각 rmin_view, lmin_view에 담음
            if rv1 < rv2:
                rmin_view = rv1
            else:
                rmin_view = rv2
            if lv1 < lv2:
                lmin_view = lv1
            else:
                lmin_view = lv2
            # print(f'rmin_view:{rmin_view}')    
            # print(f'lmin_view:{lmin_view}')

            # 완벽한 조망을 구하기 위해서 rmin_view, lmin_view를 비교하여 작은 값을 viewgood에 더해줌.
            if rmin_view < lmin_view:
                viewgood += rmin_view
            else:
                viewgood += lmin_view    
    print(f"#{test_case} {viewgood}")