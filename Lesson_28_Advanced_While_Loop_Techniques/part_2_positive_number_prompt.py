continue_loop = True
num = 0

while continue_loop:
    try:
        num = int(input("Enter a positive number (or -1 to exit): "))
        if num == -1:
            continue_loop = False
        elif num < 0:
            print("Please enter a positive number.")
        else:
            print(f"You entered: {num}")
    except ValueError:
        print("That's not a valid number! Please try again.")
