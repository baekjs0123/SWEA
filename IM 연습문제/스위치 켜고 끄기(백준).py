# 스위치 개수 입력
N = int(input())

# 스위치 상태 입력
switch = list(map(int, input().split()))

# 학생 수 입력
stu = int(input())

# 학생들의 성별과 받은 수 입력
students = [list(map(int, input().split())) for _ in range(stu)]

# 스위치 상태 변경 함수
def toggle_switch(switch, index):
    switch[index] = 1 - switch[index]

# 학생들의 명령 처리
for gender, num in students:
    if gender == 1:  # 남학생의 경우
        for i in range(num - 1, N, num):
            toggle_switch(switch, i)
    elif gender == 2:  # 여학생의 경우
        index = num - 1
        toggle_switch(switch, index)
        k = 1
        while index - k >= 0 and index + k < N and switch[index - k] == switch[index + k]:
            toggle_switch(switch, index - k)
            toggle_switch(switch, index + k)
            k += 1

# 결과 출력 (20개씩 줄바꿈)
for i in range(0, N, 20):
    print(' '.join(map(str, switch[i:i+20])))
