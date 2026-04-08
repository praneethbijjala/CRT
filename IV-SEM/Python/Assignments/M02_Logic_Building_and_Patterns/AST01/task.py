def count_digits(n: int) -> int:
    n = str(abs(n))
    count = 0
    for i in n:
        count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))