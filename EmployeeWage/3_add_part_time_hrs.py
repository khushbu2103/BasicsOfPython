import random

def emp_attandance():
    wage_par_hr = 20
    full_time = 1
    part_time = 2
    random_num = random.randint(0,2)
    if full_time == random_num:
        print("full time employee is present")
        emp_hrs = 8
       
    elif(part_time == random_num):
        print("part time employee is present")
        emp_hrs = 4
    else:
        print("absent")
        emp_hrs = 0

    emp_wage = wage_par_hr*emp_hrs
    print(f"daily eployee wage: {emp_wage}")

def main():
    emp_attandance()

if __name__ == "__main__":
    main()