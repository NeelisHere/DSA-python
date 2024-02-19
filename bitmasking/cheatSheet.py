import math

def toBin(x, maxb=64):
    res = ''
    for i in range(maxb):
        res += '1' if (x & (1 << i)) else '0'
    return ''.join(list(reversed(res)))

max_bits = lambda n: math.ceil(math.log2(n + 1))
get_bit = lambda n, i: 1 if (n & (1 << i)) else 0
isOdd = lambda n: bool(n & 1)
multiply_2powk = lambda n, k: n << k
divide_2powk = lambda n, k: n >> k
isPower2 = lambda n: bool(n & (n - 1) == 0)

def set_bit(n, i):
    n |= (1 << i)
    return n

def clear_bit(n, i):
    n &= ~(1 << i)
    return n

def clear_rightmost_bit(n):
    n &= (n - 1)
    return n

def toggle_bit(n, i):
    n ^= (1 << i)
    return n

def clear_lastk(n, k):
    n &= (-1 << k)
    return n

def clear_range(n, l, r):
    n &= (-1 << (l + 1)) | ~(-1 << (r - 1))
    return n

def count_set_bits(n):
    count, x = 0, n
    while x:
        x &= (x - 1)
        count += 1
    return count
