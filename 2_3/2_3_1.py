def gcd(a, b):
    while a != b:
        if a%b == 0:
            return b
        if b%a == 0:
            return a
        
        if a>b:
            a %= b
        elif b>a:
            b %= a
    return a

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
