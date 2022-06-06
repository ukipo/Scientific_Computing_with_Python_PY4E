# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6    F

# Input score
scor = input('Enter score: ')

# Check if number
try:
    scor = float(scor)
except:
    print('Bad score: please enter a numeric value')
    quit()

# Check if number is between 0 and 1
if scor > 1 or scor < 0:
    print('Bad score: please enter a number between 0 and 1')
    quit()

# Define scale
if scor < 0.6:
    print('F')
elif scor < 0.7:
    print('D')
elif scor < 0.8:
    print('C')
elif scor < 0.9:
    print('B')
else:
    print('A')