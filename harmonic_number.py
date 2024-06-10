def harmonic_series(num):
    for i in range(num+1):
        print(f"{i} \ {num} , ", end=" ")
    
def main():
    harmonic_series(num=5)

if __name__ == "__main__":
    main()