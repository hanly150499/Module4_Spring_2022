"""Open the editor of your choice. Write a function called hourly_employee_input that asks the user for a name (string), hours worked (int) and an hourly pay rate (float) and prints a string including the information. Include a docstring as your first line declaring what the function does.
Run the script in a shell.
Call the function, entering expected values, numbers in appropriate range
Call the function, entering negative numbers
Call the function, entering bad input (letters, symbols)
What do you need to add to your function for bad input? Handle the bad input
Submit your screen shot and .py file.
"""
def hourly_employee_input():
    fullname = str(input("Please enter your full name"))
    hours_worked = int(input("Enter your hours worked"))
    hourly_pay_rate = float(input("Enter your hourly pay rate"))
    try:
        total_hours_worked = int(hours_worked);
        if (total_hours_worked < 0 or total_hours_worked > 200):
            raise ValueError
    except ValueError:
             print("Need to contact to upper manager")
hourly_employee_input()






