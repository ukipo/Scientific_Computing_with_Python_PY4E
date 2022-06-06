# Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

# Find the colon character
indx = str.find(':')

# Slice to extract string after the colon
slstr = str[indx+1 :]

# Convert to floating point number
fstr = float(slstr)

# Print resulting floating point number
print(fstr)