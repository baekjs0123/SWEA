import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    '''
    접근법
    nums 배열과 new_nums라는 빈 리스트를 만들고 nums를 오름차순으로 정렬. 
    nums 에서 가장 작은 수 = nums의 0번째, 가장 큰 수는 nums의 -1번째
    pop()메서드를 활용하여 max_num과 min_num을 추출하여 새로운 리스트 new_nums에 추가해준다. 
    '''
    # nums 오름차순 정렬
    nums.sort()
    # 빈 리스트 생성
    new_nums = []
    for i in range(5):
        # pop()으로 최대값, 최소값 추출
        max_num = nums.pop(-1)
        # 새로운 리스트에 추가한다.
        new_nums.append(max_num)
        min_num = nums.pop(0)
        new_nums.append(min_num)

    print(f'#{tc}' , *[num for num in new_nums])



