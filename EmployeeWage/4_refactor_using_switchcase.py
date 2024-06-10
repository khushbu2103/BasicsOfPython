import random

def emp_attandance():
    wage_par_hr = 20
    full_time = 1
    part_time = 2
    def full_time_emp():
        emp_hrs = 8
        print("Full time employee is present")
        return emp_hrs

    def part_time_emp():
        emp_hrs = 4
        print("Part time employee is present")
        return emp_hrs

    def absent_emp():
        emp_hrs = 0
        print("Employee is absent")
        return emp_hrs

    switch_case = {
        full_time: full_time_emp,
        part_time: part_time_emp
    }

    random_num = random.randint(0, 2)
    emp_hrs = switch_case.get(random_num, absent_emp)()
    
    emp_wage = wage_par_hr * emp_hrs
    print(f"Daily employee wage: {emp_wage}")

    
def main():
    emp_attandance()

if __name__ == "__main__":
    main()