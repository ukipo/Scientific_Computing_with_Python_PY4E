# Calculate pay with 2.5 pay over 40 hours
# Enter hours
hrs = input('Enter Hours: ')

# Enter rate
rate = input('Enter Rate: ')

# Calculate pay
if float(hrs) < 40:
    pay = float(hrs) * float(rate)
else:
    basepay = 40 * float(rate)
    overtime = (float(hrs) - 40)
    overtimepay = overtime * (float(rate) * 1.5)
    pay = basepay + overtimepay

# Print results
print('Pay:', pay)