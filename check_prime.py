def is_prime(x):
    """Return True if the number is prime"""
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

def print_next_prime(number):
    """Print the closes prime number larger than *number*"""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
