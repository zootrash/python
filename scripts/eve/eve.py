#!/usr/bin/python3
#
# Eve: The personal and mysterious AI
#
####################
#
# eve pre-alpha
#
####################

# libraries
import time		# time of OS

# loop counter
hello = 1

# date
__DATE__ = time.strftime("Today's date is %B %d, %Y.")

# time
__TIME__ = time.strftime("The time is currently %I:%M %p.")


# eve loop
print('Yes?')
while(hello):

	userinput = input('\n')

	if "no" in userinput:
		print('Farewell.')
		hello = 0

	if(hello == 1):
		# testing user input
		if "date" in userinput:
			print(__DATE__)
		elif "time" in userinput:
			print(__TIME__)
		else:
			print('I am unable to reply to your comment.')

		print('Anything else?')

