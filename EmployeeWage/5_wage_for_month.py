import random

def emp_attandance():
    wage_par_hr = 20
    working_days = 20
    full_time = 1
    part_time = 2
    total_wage = 0
    for i in range(working_days):
        def full_time_emp():
            emp_hrs = 8
            return emp_hrs

        def part_time_emp():
            emp_hrs = 4
            return emp_hrs

        def absent_emp():
            emp_hrs = 0
            return emp_hrs

        switch_case = {
            full_time: full_time_emp,
            part_time: part_time_emp
        }

        random_num = random.randint(0, 2)
        emp_hrs = switch_case.get(random_num, absent_emp)()
        emp_wage = wage_par_hr * emp_hrs
        total_wage+=emp_wage
        print(f"Daily employee wage: {emp_wage}")

    print(f"total employeewage for: {working_days} working is: {total_wage}")

    
def main():
    emp_attandance()
    

if __name__ == "__main__":
    main()