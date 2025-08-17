grades = []
while True:
    grade = input("Enter a grade (or type 'done' to finish): ")
    if grade.lower() == 'done':
        break
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            print("Invalid grade, please enter a number between 0 and 100.")
            continue  # Skip this iteration
        grades.append(grade)
    except ValueError:
        print("That’s not a valid grade!")

print("Entered grades:", grades)
