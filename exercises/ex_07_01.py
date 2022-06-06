# Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

# Open file
fhand = open('mbox-short.txt')

# Read file line by line
for line in fhand:
    # Strip line breaks from end of line
    line = line.rstrip()
    # print line in upper case
    print(line.upper())