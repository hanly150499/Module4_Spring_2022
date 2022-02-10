"""You can now update your average test scores code from a previous assignment with added input validation using try/except.
Details:
Update your previous assignment code to include try/except for each of the user inputs.
If the user enters negative numbers or a string for their number inputs, the except path should print an error message.
Submit your .py file.
This is worth 10 points.
"""
fullname = str(input("Please enter your fullname"))
age = int (input("Please enter your age"))
reading_scores = float(input("Please enter your scores"))
writting_scores = float(input("Please enter your scores"))
speaking_scores = float(input("Please enter your scores"))
try:
    scores1 = float(reading_scores)
    scores2 = float(writting_scores)
    scores3 = float(speaking_scores)
    if (scores1 > 0):
        print(scores1)
    else:
        raise ValueError('Negative number')
    if(scores2 > 0):
        print(scores2)
    else:
        raise ValueError('Negative number')
    if (scores3 > 0):
        print(scores3)
    else:
        raise ValueError('Negative number')
except:
    print('Error message')
finally:
    Total = reading_scores + writting_scores + speaking_scores
    Total2 = Total/3
    print(Total2)
    print('full name is:',fullname,'age:',age,'average scores is:',Total2)




