import random

def emp_attandance():
    random_num = random.randint(0,1)
    if random_num == 0:
        print("present")
    else:
        print("absent")

def main():
    emp_attandance()

if __name__ == "__main__":
    main()