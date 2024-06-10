import random


def Flip_Coin(num_flip):
    if num_flip <= 0:
        raise ValueError("The number of flips must be a positive integer.")
    head = 0
    tail = 0
    for _ in range(num_flip):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    heads_percentage = (heads / num_flip) * 100
    tails_percentage = (tails / num_flip) * 100
    return heads_percentage, tails_percentage


def main():
    num_flip = int(input("Enter the number of times to flip the coin: "))
    heads_percentage, tails_percentage = Flip_Coin(num_flip)
    print(f"Percentage of Heads: {heads_percentage:.2f}%")
    print(f"Percentage of Tails: {tails_percentage:.2f}%")


if __name__ == "__main__":
    main()
    
  
    