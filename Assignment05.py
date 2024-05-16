# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# IB,5/12/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ""  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")
    student = json.load(file)
    for row in file.readlines():
        # Transform the data from the json file
        student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course': course_name}
        # Load it into our collection (list of dictionary rows)
        students.append(student_data)
except FileNotFoundError as e:
    print("The file must exist before running this script!\n")
    print(e, e.__doc__)
except Exception as e:
    print("There was a non-specific error!\n")
    print(e, e.__doc__)
finally:
    if file.closed is False:
        file.close()
    # file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise Exception("Please only use alphabetic letters for your first name")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise Exception("Please only use alphabetic letters for your last name")
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name,
                            'course': course_name}
            students.append(student_data)
            for row in students:
                print(f'{row["first_name"]} {row["last_name"]} is registered for {row["course"]}')
        except Exception as e:
            print(e, e.__doc__)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for row in students:
            json_data = f'{row["first_name"]} {row["last_name"]} is registered for {row["course"]}'
        print(json_data)
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
        except FileNotFoundError as e:
            print("The file must exist before running this script!\n")
            print(e, e.__doc__)
        except Exception as e:
            print("There was a non-specific error!\n")
            print(e, e.__doc__)
        finally:
            if file.closed is False:
                file.close()
        print("The following data was saved to file!")
        for row in students:
            print(json_data)
            continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
