def find_odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
        

def main():
    num = int(input("enter a number"))
    find_odd_even(num)


if __name__ == "__main__":
    main()