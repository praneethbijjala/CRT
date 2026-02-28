import math

def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    # Calculate average
    avg = (n1 + n2 + n3) / 3

    # Truncate to 2 decimal places
    avg = math.floor(avg * 100) / 100

    # Format average
    if avg.is_integer():
        avg_str = f"{avg:.1f}"
    else:
        avg_str = f"{avg:.2f}"

    # Pass / Fail condition
    status = "Pass" if avg >= 40 else "fail"

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))