# Worksheet 1.2: Task 1 Solution
grade = input("Please enter your grade:")
if not grade.isdecimal() or grade <0 or grade >100:
    import sys
    sys.exit("Error: Grade must be an integer between 0 and 100")
elif grade >=0 and grade <=39:
     print(f"{grade} is a Fail")
elif grade >=40 and grade <=69:
     print(f"{grade} is a Pass")
elif grade >=70 and grade <=100:
     print(f"{grade} is a Distinction")