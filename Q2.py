def max_of_three(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	else:
		return c
try:
	a=int(raw_input("Enter first number "))
except ValueError:
	print "Input is not a number"
	exit(1)
try:
	b=int(raw_input("Enter second number "))
except ValueError:
	print "Input is not a number"
	exit(1)
try:
	c=int(raw_input("Enter third number "))
except ValueError:
	print "Input is not a number"
	exit(1)
print "Largest number is %d"%max_of_three(a,b,c)
