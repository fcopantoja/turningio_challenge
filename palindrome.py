
def base10_to_n(n, base):
    _list = []
    while n:
        _list.append(n % base)
        n = n // base
    return ''.join(str(x) for x in reversed(_list))


def is_palindrome(input):
    return input == input[::-1]


def lowest_base_palindrome(n):
    for j in range(2, 1000):
        num = base10_to_n(n, j)
        if is_palindrome(num):
            return num, j
    return None, None

if __name__ == '__main__':
    for i in range(1, 1001):
        palindrome, base = lowest_base_palindrome(i)
        if palindrome:
            print('{} in base {} is palindrome ({})'.format(i, base, palindrome))
