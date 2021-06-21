# if a single quote is in the string,then:-
from typing import Text


print('bobby\'s world')
print("bobby's world")
# same for double quotes

Message = "Hello World!"

# Length of string:-
print(len('Python'))

print(Message[6])
# if index out of bound, returns -1

# string slicing
print(Message[0:5])  # or
print(Message[:5])
print(Message[6:12])  # or
print(Message[6:])

print(Message[0:12:2])
# skipping one index and printing the message

# some string methods :

print(Message.isalnum())
print(Message.lower())
print(Message.upper())
print(Message.count("o"))
print(Message.find("World!"))

print(Message.replace("World!", "Universe!"))

# Formatting

greeting = 'Hello'
name = 'Animesh'

message = greeting + ', ' + name + '. Welcome!'
print(message)
# This Method is complex and hard to keep track of.

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# This Method is comparitively easy.

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
# This Method is New feature called f'string and althemore easy(above Py3.6 version)

tag = "h1"
text = 'this is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
# this placing of 0's and 1's in place holders declares the args in format to be placed at the given index loc.

for i in range(1, 11):
    print('the value is {:04}'.format(i))
# specifying the number of digits to bi printed. vvvvvv

pi = 3.1412637495
print('value of pi is {:.4f}'.format(pi))
# specifying the number of decimal places to be printed.

print('1MB is equal to {:,.2f} Bytes'.format(1000**2))
# this specified the comma seperator for the numeric and 2 decimal places.


# dir function shows all ther functions related to the variable.
# print(dir(message))
# help fucntion shows all functions related to the variable in very detailed order.
# print(help(int))
# print(help(str.lower()))
