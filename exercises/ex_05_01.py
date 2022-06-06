#  Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Define empty variables for counting and sum of numbers
count = 0
sum = 0

# Infinite loop: while loop to keep entering numbers until loop is broken
while True:
    # Input: enter a number
    entry = input('Enter a Number: ')
    # Exit mechanism: check if done to break loop
    if entry == 'done':
        break
    # Sanity check: check if entry is a number
    try:
        entry = float(entry)
    except:
        print('Invalid input')
        continue # Go back to the top of the loop without executing remaining lines in loop
    # Count the entry number and sum the values
    count = count+1
    sum = sum+entry

# Print out the count, sum and average
print(sum, count, sum/count)

    

# Step by step what is used
# # Enter number
# entry = input('Enter a Number: ')

# # Check if entry is a number
# try:
#     entry = int(entry)
# except:
#     print("Invalid input")

# # Check if done
# if entry is 'done':
#     quit()

# # Count and average for loop
# count = 0
# sum = 0

# for i in entry_list:
#     count = count + 1
#     sum = sum + i
# print(sum, count, sum/count)
