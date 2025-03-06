# import sys
# sys.stdin = open('input.txt', 'r')

def hex_to_demical(hex_num):
    hex_digits = '0123456789ABCDEF'
    decimal_num = 0
    pow = 0

    for digit in reversed(hex_num):
        decimal_num += hex_digits.index(digit) * (16 ** pow)
        pow += 1
    return decimal_num

def decimal_to_binary(decimal_num):
    binary_num =  ''
    if decimal_num == 0:
        return '0'
    while decimal_num > 0:
        remain = decimal_num % 2
        binary_num = str(remain) + binary_num
        decimal_num //= 2
    binary_num_remain = len(binary_num) % 4
    if binary_num_remain != 0:
        binary_num = '0' * (4 - binary_num_remain) + binary_num

    return binary_num



T = int(input())
for tc in range(1, T + 1):
    N, hex_num = map(str, input().split())
    decimal = hex_to_demical(hex_num)
    binary = decimal_to_binary(decimal)

    print(f'#{tc} {binary}')
