# Calculate pay with 2.5 pay over 40 hours with try and except
# Enter hours
hrs = input('Enter Hours: ')
try:
    hrs = float(hrs)
except:
    print('Error, please enter numeric input')
    quit()

# Enter rate
rate = input('Enter Rate: ')
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

# Calculate pay
if hrs < 40:
    pay = hrs * rate
else:
    basepay = 40 * rate
    overtime = (hrs - 40)
    overtimepay = overtime * (rate * 1.5)
    pay = basepay + overtimepay

# Print results
print('Pay:', pay)