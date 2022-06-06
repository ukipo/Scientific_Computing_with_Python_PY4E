# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Calculate pay with 2.5 pay over 40 hours with try and except
# Enter hours
hrs = input('Enter Hours: ')
try:
    hrs = float(hrs)
except:
    print('Error, please enter numeric input')
    quit()

# Enter rate
rte = input('Enter Rate: ')
try:
    rte = float(rte)
except:
    print('Error, please enter numeric input')
    quit()

# Define function called computepay which takes two parameters (hours and rate)
def computepay(hours, rate):
    # Calculate pay
    if hours < 40:
        pay = hours * rate
    else:
        basepay = 40 * rate
        overtime = (hours - 40)
        overtimepay = overtime * (rate * 1.5)
        pay = basepay + overtimepay
    
    # Return
    return(pay)

# Print results
print('Pay:', computepay(hrs, rte))