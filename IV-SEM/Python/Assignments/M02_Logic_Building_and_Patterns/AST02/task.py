def reverse_number(n: int) -> int:
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))