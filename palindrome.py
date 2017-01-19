
def base10_to_n(n, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''

    try:
        n = int(n)
        base = int(base)
    except:
        return result

    if n < 0 or base < 2 or base > 36:
        return result

    while True:
        r = n % base
        result = digits[r] + result
        n /= base
        if n == 0:
            break

    return result


def is_palindrome(input):
    return input == input[::-1]


def lowest_base_palindrome(n):
    for j in range(2, 17):
        num = base10_to_n(n, j)
        if is_palindrome(num):
            return num, j
    return None, None


if __name__ == '__main__':
    for i in range(1, 1001):
        palindrome, base = lowest_base_palindrome(i)
        if palindrome:
            print('{} in base {} is palindrome ({})'.format(i, base, palindrome))
