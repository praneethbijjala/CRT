def number_triangle(n: int) -> str:
    pattern = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            pattern += str(j)
        if i != n:
            pattern += "\n"
    return pattern

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))