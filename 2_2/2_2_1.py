#Дано целое число 1≤n≤40 1 \le n \le 40 1≤n≤40, необходимо вычислить n n n-е число Фибоначчи (напомним, что F0=0 F_0=0 F0​=0, F1=1 F_1=1 F1​=1 и Fn=Fn−1+Fn−2 F_n=F_{n-1}+F_{n-2} Fn​=Fn−1​+Fn−2​ при n≥2 n \ge 2 n≥2)
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        fn_2 = 0
        fn_1 = 1
        i = 2
        while i <= n:
            x = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = x
            i += 1
        return fn_1
        

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
