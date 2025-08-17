with open('example.txt', 'w') as file:
    file.write('Hello, world!')
class CustomContext:
    def __enter__(self):
        print("Entering the context...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")

with CustomContext():
    print("Inside the context.")
