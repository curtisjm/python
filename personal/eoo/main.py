try:
    low = input("Enter a lower bound: ")
    low = int(low)
    high = input("Enter a higher bound: ")
    high = int(high)

    for i in range(low, high, 4):
        print(f"{i} ", end="")
except:
    print("Invalid number.")
