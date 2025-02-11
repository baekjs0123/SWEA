import sys
sys.stdin = open('../0211_String/sample_input.txt', 'r')

T = int(input())
N = int(input())
nums = list(map(int, input().split()))

'''
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 
10 1 9 2 8 3 7 4 6 5

접근법
nums 배열과 new_nums라는 똑같은 배열을 만들고 가장 큰 수를 정렬하면 new_nums 배열에서 해당 수를 제거한다.
new_nums 에서 가장 작은 수를 찾아 nums에서 정렬하고 new_nums에 가장 작은 수는 제거한다.
다시 new_nums에서 가장 큰수를 찾으면 nums기준에서는 2번째로 큰 수가 된다. 이를 new_nums가 []가 될때 까지 반복한다.
'''
new_nums = nums[:]
for i in range(len(nums)):
    max_num = nums[i]
    min_num = nums[i]
    for j in range(len(new_nums)):
        if max_num < new_nums[j]:
            max_num = new_nums[j]

            new_nums.pop()
        if min_num > new_nums[j]:
            min_num = new_nums[j]
            new_nums.pop()


