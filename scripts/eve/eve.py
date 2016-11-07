#/usr/bin/python3
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

def goodbye(userInput)
	"Farewell Eve"
	if "no" in userInput
		print('Farewell.')
		return 0

def respond(userInput):
	"Respond to user input"

	goodbye(userInput)


# eve loop
print('Yes?')
while(hello):

	userInput = input('\n')
	hello = respond(userInput)

	if(hello == 1):
		# testing user input
		if "date" in userInput:
			print(__DATE__)
		elif "time" in userInput:
			print(__TIME__)
		else:
			print('I am unable to reply to your comment.')

		print('Anything else?')

