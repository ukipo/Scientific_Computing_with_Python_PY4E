# Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# X-DSPAM-Confidence:0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

# Import re
import re

# Ask for file
file = input('Enter the file name: ')

# Create list to save spam confidence values
spamlist = list()

# Open file + sanity check
try:
    fhand = open(file)
except:
    print("Could not open file")
    quit()
#fhand = open('mbox-short.txt')

# Read through file line by line
for line in fhand :
    # Strip whitespace from end of lines
    line = line.rstrip()
    # Extract line that starts with "X-DSPAM-Confidence: " with
        # .starswith
    # if line.startswith('X-DSPAM-Confidence: ') :
        # re.findall
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # Continue if not found
    if len(stuff) != 1 : continue
    # Convert into float
    stuff = float(stuff[0])
    # Append value to list
    spamlist.append(stuff)

# Count the number of spam confidence values
counts = len(spamlist)

# Compute total of spam confidence values
totals = sum(spamlist)

# Print average spam confidence value
print("Average spam confidence:", totals/counts)