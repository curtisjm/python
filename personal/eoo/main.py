try:
    low = input("Enter a lower bound: ")
    low = int(low)
    high = input("Enter an upper bound: ")
    high = int(high)

    if low % 2 == 0:
        low += 1

    for i in range(low, high + 1, 4):
        print(f"{i}, ", end="")
except:
    print("Invalid number.")
