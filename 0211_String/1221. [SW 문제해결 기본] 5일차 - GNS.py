import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())


def find_key(d, t_value):
    for key, value in d.items():
        if value == t_value:
            return key


for tc in range(T):
    tc, N = map(str, input().split())
    N = int(N)
    num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    arr = input().split()
    for i in range(len(arr)):
        if arr[i] in num_dict:
            arr[i] = num_dict[arr[i]]
    arr.sort()
    for i in range(len(arr)):
        if arr[i] in num_dict.values():
            arr[i] = find_key(num_dict, arr[i])

    print(tc)
    print(' '.join(arr))
