#!/usr/bin/python3

'''The UTF-8 validation module.
'''


def validUTF8(data):
    '''Check to match a list of integers to be valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    '''
    ignore = 0
    num = len(data)
    for x in range(num):
        if ignore > 0:
            ignore -= 1
            continue
        if type(data[x]) != int or data[x] < 0 or data[x] > 0x10ffff:
            return False
        elif data[x] <= 0x7f:
            ignore = 0
        elif data[x] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span_val = 4
            if num - x >= span_val:
                nxt_body = list(map(
                    lambda xx: xx & 0b11000000 == 0b10000000,
                    data[x + 1: x + span_val],
                ))
                if not all(nxt_body):
                    return False
                ignore = span_val - 1
            else:
                return False
        elif data[x] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span_val = 3
            if num - x >= span_val:
                nxt_body = list(map(
                    lambda xx: xx & 0b11000000 == 0b10000000,
                    data[x + 1: x + span_val],
                ))
                if not all(nxt_body):
                    return False
                ignore = span_val - 1
            else:
                return False
        elif data[x] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span_val = 2
            if num - x >= span_val:
                nxt_body = list(map(
                    lambda xx: xx & 0b11000000 == 0b10000000,
                    data[x + 1:  + span_val],
                ))
                if not all(nxt_body):
                    return False
                ignore = span_val - 1
            else:
                return False
        else:
            return False
    return True
