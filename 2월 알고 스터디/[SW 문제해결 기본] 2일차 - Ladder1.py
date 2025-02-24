import sys
sys.stdin = open('input.txt', 'r')

'''
접근법
먼저 골인지점 2를 찾는다. 골인 지점으로부터 사다리의 맨 위까지 거꾸로 거슬러 올라간다.
쭉 올라가다가 좌, 우에 1이 있으면 1이 있는 방향으로 꺾어서 직진한다.
쭉 직진하다가 0을 만나면 위로 다시 직진한다.
반복하면서 i(행번호)가 0이 되면 출발점 찾았다!! j(열번호)를 출력해준다.
'''
# # 골인지점 찾는 함수
# def find_goal():
#     for j in range(100):
#         if ladder[99][j] == 2:
#             return j
#
# # 유효성 검사
# def is_valid(i, j):
#     return 0 <= i < 100 and 0 <= j < 100 and ladder[i][j] == 1
#
#
# for _ in range(10):
#     tc = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     goal = find_goal()
#
#     # 골인 지점으로부터 거슬러 올라가기 때문에 i = 99, j = goal
#     i, j = 99, goal
#
#     # i가 0이 될때 까지 반복문
#     while i >= 0:
#         # 왼쪽에 길이 있을 때
#         if is_valid(i, j - 1):
#             while is_valid(i, j - 1):
#                 j -= 1
#             i -= 1
#         # 오른쪽에 길이 있을 때
#         elif is_valid(i, j + 1):
#             while is_valid(i, j + 1):
#                 j += 1
#             i -= 1
#         # 양쪽다 길이 없을 때
#         else:
#             i -= 1
#
#     print(f'#{tc} {j}')



# 골인지점 찾는 함수
def find_goal():
    for j in range(100):
        if ladder[99][j] == 2:
            return j

# 유효성 검사
def is_valid(i, j):
    return 0 <= i < 100 and 0 <= j < 100 and ladder[i][j] == 1

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    goal = find_goal()

    # 골인 지점으로부터 거슬러 올라가기 때문에 i = 99, j = goal
    i, j = 99, goal

    stack = []
    # i가 0이 될때 까지 반복문
    while i >= 0:
        for di, dj in [[1, 0],[0, -1],[0, 1]]:
            ni = di + i
            nj = dj + j
            # 왼쪽에 길이 있을 때
            if is_valid(ni, nj) and is_valid(ni, nj -1):
                j -= 1
                stack += i
            # 오른쪽에 길이 있을 때
            elif is_valid(ni, nj) and is_valid(ni, nj + 1):
                j += 1
            # 양쪽다 길이 없을 때
            else:
                i -= 1

    print(f'#{tc} {j}')
