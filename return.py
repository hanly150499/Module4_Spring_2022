"""Open the editor of your choice. Make a copy of your .py file containing the function called hourly_employee_input that asks the user for a name (string), hours worked (int) and an hourly pay rate (float) and prints a string including the information.
Write a function weekly_pay that accepts in the parameter list the hours_worked and hourly_pay_rate and returns the calculated weekly pay.
Make a function call in hourly_employee_input
Change the string in hourly_employee_input  to print name and weekly pay
Change the hourly_employee_input instead of printing, return a statement and print the result in the main
Include a docstring as your first line declaring what the function does.
Submit your .py file
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
def weekly_pay(hours_worked,hourly_pay_rate):
    return hours_worked*hourly_pay_rate
total = weekly_pay(40,12)
print('Weekly pay is',total)



