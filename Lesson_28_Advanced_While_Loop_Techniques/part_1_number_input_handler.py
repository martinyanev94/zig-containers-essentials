def get_input():
    try:
        return int(input("Enter a number (or type 'exit' to quit): "))
    except ValueError:
        return "Error: Invalid input"

result = ""
while True:
    result = get_input()
    if isinstance(result, int):
        print(f"You entered: {result}")
        if result > 10:
            print("That's quite a large number!")
    else:
        print(result)  # Handle the error message
        break  # Exit on error
