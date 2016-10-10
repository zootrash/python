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

# get user input
userinput = input('Yes?\n\n')

# date
__DATE__ = time.strftime("Today's date is %B %d, %Y")
print(__DATE__)

# time
__TIME__ = time.strftime("The time is currently %I:%M %p")
print(__TIME__)
