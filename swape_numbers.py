def swap_twonumbers(num1, num2):
    sum = num1+num2
    num1 = sum - num1
    num2 = sum - num2
    print(f"num1: {num1}, num2: {num2}")

def main():
    # num1 = int(input("enter num1"))
    # num2 = int(input("enter num2"))
    num1, num2 = map(int, input("Enter num1 and num2 separated by space: ").split())
    swap_twonumbers(num1, num2)

if __name__ == "__main__":
    main()