# get string input
total = raw_input("Enter total amount: ")

# get integer input: int() convert string to integer
# float() convert string to floating number
tip_rate = int(raw_input("Enter tip rate (such as 0.15): "))

pay = total + total*tip_rate

# use string formatting to output result
print "You should pay: " + pay
