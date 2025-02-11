import sys
sys.stdin = open('sample_input.txt', 'r')
def is_valid(Ci,N):
    Ci_onebox = N / 3
    result = Ci_onebox <= N/2
T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    Ci = list(map(int, input().split()))

    small = []
    mid = []
    large = []
    Ci_onebox = N / 3
    for i in range(len(Ci)):
        if Ci[i] not in Ci[i+1: (i+1) + (Ci_onebox - 1)]:
            small.append()

