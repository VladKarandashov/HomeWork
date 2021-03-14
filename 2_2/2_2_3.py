def fib_mod(n, m):
    if n == 0: return 0%m
    elif n == 1: return 1%m
    else:
        l = [0]
        fn_2 = 0
        fn_1 = 1
        i = 2
        while True:
            x = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = x%m
            if (fn_2 == 0) and (fn_1 == 1):
                t = i-1
                break
            else:
                l.append(fn_2)
                
            i += 1

        return l[n%t]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
