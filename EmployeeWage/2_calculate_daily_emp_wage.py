import random

def emp_attandance():
    wage_par_hr = 20
    full_day_hr = 8
    random_num = random.randint(0,1)
    if random_num == 0:
        print("present")
        emp_wage = wage_par_hr*full_day_hr
        print(f"daily eployee wage: {emp_wage}")
    else:
        print("absent")

def main():
    emp_attandance()

if __name__ == "__main__":
    main()