def leap_year(year):
    if ((year%4 == 0 and year%100==0) or (year%400 ==0)):
        print(f"{year}  is leap year")
    else:
        print(f"{year} is not leap year")

# Get the year input from the user
year = int(input("Enter a year: "))

# Call the function with the user input
leap_year(year)