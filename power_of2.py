def print_powers_of_2(N):
    # Check if N is within the valid range
    if N < 0 or N >= 31:
        print("The power value N must be between 0 and 30 (inclusive).")
    for i in range(N+1):
        print(f"power of 2: {2**i}")

num = int(input("enter the exponent"))
print_powers_of_2(num)