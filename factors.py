def get_factors(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(f"factors: {i}")

def main():
    num = int(input("number: "))
    get_factors(num)

if __name__ == "__main__":
    main()