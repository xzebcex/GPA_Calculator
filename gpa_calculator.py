# GPA Calculator.

print('Hello and welcome to the GPA calculator.')
print('Please enter each letter grade on a separate line.\nTo indicate the end, enter a blank.')

# Convert a letter grade to a point value.
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0,
          'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33,
          'D': 1.0, 'F': 0.0}

num_courses = 0
total_points = 0
done = False
while not done:
    grade = input().upper()  # Read a line from the user.
    if grade == '':  # A blank line was inserted.
        done = True
    elif grade not in points:  # Unidentified grade entered.
        print("Unknown grade {0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
    if num_courses > 0:  # Try not to divide by zero.
    print('Your GPA is {0:.3}'.format(total_points / num_courses))
