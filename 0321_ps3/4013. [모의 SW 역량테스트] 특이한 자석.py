import sys
sys.stdin = open('input.txt', 'r')
'''
1. 빨간색 화살표 위치가 0번째 인덱스이다. 따라서 자석이 서로 붙어있는 날의 인덱스번호는
2가 오른쪽, 왼쪽은 6번 인덱스이다.

2. 자석이 마지막 자석이 아닐때 magnetism[i][3] != magnetism[i + 1][6]이면 자석이 회전하고 같다면 회전되지 않는다.
자석이 회전할때 왼쪽자석이 회전하는 방향의 반대 방향으로 오른쪽 자석이 회전한다.

3. 만약 있는 자석중에 회전하지 않는 자석이 있다면 그 뒤에 모든 자석은 회전하지 않는다.

4. 모든 회전이 끝난 후 magnetism[i][0] 이 N극이면 0점, S극이면 각 자석마다 1, 2, 4, 8점을 획득한다.
'''
T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    magnet_info = [list(map(int, input().split())) for _ in range(4)]
    for i in range(K):
        magnet_num, spin_dir = map(int, input().split())
        magnet_num -= 1 # 인덱스는 0부터 시작이라 -1한다.
        check = []
        for j in range(4):
            if j != 3:
                if magnet_info[j][2] != magnet_info[j + 1][6]:
                    check.append(1)
                else:
                    check.append(0)
            else:
                if magnet_info[j][6] != magnet_info[j - 1][2]:
                    check.append(1)
                else:
                    check.append(0)
        if check[magnet_num]:
            if magnet_num % 2 == 1:
                odd_even = 'odd'
            else:
                odd_even = 'even'
            if spin_dir == 1:
                magnet_info[magnet_num].insert(0, magnet_info[magnet_num].pop())
                for k in range(4):
                    if k == magnet_num:
                        continue
                    if odd_even == 'odd' and k % 2 == 1:
                        magnet_info[k].insert(0, magnet_info[k].pop())
                    elif odd_even == 'odd' and k % 2 == 0:
                        magnet_info[k].insert(-1, magnet_info[k].pop(0))
                    if odd_even == 'even' and k % 2 == 0:
                        magnet_info[k].insert(0, magnet_info[k].pop())
                    elif odd_even == 'even' and k % 2 == 1:
                        magnet_info[k].insert(-1, magnet_info[k].pop(0))
            else:
                magnet_info[magnet_num].insert(-1, magnet_info[magnet_num].pop(0))
                for k in range(4):
                    if k == magnet_num:
                        continue
                    if odd_even == 'odd' and k % 2 == 1:
                        magnet_info[k].insert(-1, magnet_info[k].pop(0))
                    elif odd_even == 'odd' and k % 2 == 0:
                        magnet_info[k].insert(0, magnet_info[k].pop())
                    if odd_even == 'even' and k % 2 == 0:
                        magnet_info[k].insert(-1, magnet_info[k].pop(0))
                    elif odd_even == 'even' and k % 2 == 1:
                        magnet_info[k].insert(0, magnet_info[k].pop())

    total_score = 0
    for i in range(4):
        total_score += magnet_info[i][0] * (2**i)
    print(f'#{tc} {total_score}')






