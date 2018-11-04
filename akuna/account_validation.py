import math
"""
8BADF00D

9154032
24
18
18 != 0D --> F
"""
def process(line):
    first_six = line[:6]
    last_two = line[6:]
    first_six = hex_dec(first_six)
    sum_ = sum_digits(first_six)
    sum_hex = dec_hex(sum_)
    res = True if sum_hex == last_two else False
    if res: print('VALID')
    else: print('INVALID')

def hex_dec(hex):
    hex_dec_map = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    dec = 0
    pwr = 0
    for i in range(len(hex) - 1, -1, -1):
        if ord(hex[i]) <= 57:
            digit = int(hex[i])
        else:
            digit = hex_dec_map[hex[i]]
        dec += (16 ** pwr) * digit
        pwr += 1
    return dec

def dec_hex(dec):
    """
    24 % 16 = 8 -- use
    res = 24 / 16 = 1
    1 % 16 = 1 -- use
    res = 1 / 16 = 0
    """
    dec_hex_map = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    hex = []
    while dec != 0:
        tmp = dec % 16
        if tmp <= 9:
            hex = [str(tmp)] + hex
        else:
            hex = [dec_hex_map[tmp]] + hex
        dec = math.floor(dec / 16)

    hex = ''.join(hex)
    return hex

def sum_digits(num):
    res = 0
    for digit in str(num):
        res += int(digit)
    return res

if __name__ == '__main__':
    process('8BADF00D')
    process('C0FFEE1C')