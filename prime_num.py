def prime_number(n):
     if n <= 1:
         return False
     count = 0
     for i in range(1, n + 1):
        if n % i == 0:
            count+=1
     return count == 2


def main():
    num1 = 10
    num2 = 20
    for i in range(num1, num2+1):
        if prime_number(i):
            print(i, end=" ")


if __name__ == "__main__":
    main()

