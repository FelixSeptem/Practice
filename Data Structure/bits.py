# -*- coding:utf-8 -*-  

def hamming_distance(x, y):
    difference = x ^ y
    count = 0
    while difference:
        # this removes ones from right to left (least to most significant)
        difference &= difference - 1
        count += 1
    return count


# Wegner method
def hamming_weight(x):
    if x < 0:
        return None

    count = 0
    while x:
        x &= x - 1
        count += 1

    return count


def pop_count(i):
    i -= ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def is_bit_set(x, pos):
    return (x & (1 << pos)) != 0


def is_even(x):
    return x & 1 == 0


def is_power_of_2(x):
    return (x & x - 1) == 0


# Returns the n bits in bitfield starting at position pos
def get_bits(x, pos, n):
    return (x >> (pos + 1 - n)) & ~(~0 << n)


def set_bit(x, position):
    return x | (1 << position)


def clear_bit(x, position):
    return x & ~(1 << position)


def toggle_bit(x, position):
    return x ^ (1 << position)


def rotate_left(x, n):
    print(bin(-n & 31))
    return (x << n) | (x >> (-n & 31))  # assumes a 32 bit word size


def add(a, b):
    while a:
        c = b & a
        b ^= a
        c <<= 1
        a = c
    return b


def get_sign(x):
    return -(x < 0)


# has odd number of bits
def has_parity(x):
    parity = False

    while x:
        parity = not parity
        x &= (x - 1)

    return parity


def has_parity_parallel(x):
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x &= 0xf
    return (0x6996 >> x) & 1


def next_power_of_2(x):
    x -= 1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x += 1

    return x


#
# def modulo(x, y):
#     return x & ((1 << y) - 1)

# high_bit_mask will be all 1s if negative or all 0 if positive
# for negative will NOT(x) - (-1) = NOT(x) + 1, which is two's complement conversion from negative to positive
def myabs(x):
    high_bit_mask = x >> 31
    return (x ^ high_bit_mask) - high_bit_mask


def swap_ints(a, b):
    a ^= b
    b ^= a
    a ^= b
    return [a, b]