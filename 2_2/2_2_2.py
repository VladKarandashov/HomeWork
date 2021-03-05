# Дано число 1≤n≤107 1 \le n \le 10^7 1≤n≤107, необходимо найти последнюю цифру n n n-го числа Фибоначчи.

def fib_digit(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        fn_2 = 0
        fn_1 = 1
        i = 2
        while i <= n:
            x = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = x%10
            i += 1
        return fn_1


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
