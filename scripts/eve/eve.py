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

# date
__DATE__ = time.strftime("Today's date is %B %d, %Y.")

# time
__TIME__ = time.strftime("The time is currently %I:%M %p.")

# counter
question = 0

# first welcome message from eve
def welcome():
  print('Hello, my name is Eve!')

# first and next followups for eve
def ask(question):
  if(question):
    print('Anything else?')
  else:
    print('What can I do for you today?')

# return 1 for true
def setTrue():
  return 1

# print bye message and return false
def goodbye():
  print('Farewell, have a great day!')
  return False

# exit eve
def exitEve(userInput):
  if "no" in userInput:
    return goodbye()
  elif "bye" in userInput:
    return goodbye()
  else:
    return True

# check if user wants to exit
def userExit(userInput):
  return exitEve(userInput)

# responses for eve
def eveResponse(userInput):
  if "date" in userInput:
    print(__DATE__)
  elif "time" in userInput:
    print(__TIME__)
  else:
    print('I am unable to reply to your comment.')

# eve loop
welcome()
while(True):
  ask(question)
  question = setTrue()
  userInput = input('\n')

  if(userExit(userInput)):
    eveResponse(userInput)
  else:
    quit()
