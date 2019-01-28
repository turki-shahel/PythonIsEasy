'''Pirple Python is Easy course
    Homework #5 Loops "FizzBuzz"
    by Turki Shahel'''
print('Homework Assignment #5: Basic Loops')
print('By Turki Shahel')
print('='*35)
for counter in range(1,101):
    if counter % 3 == 0:
        print('[',counter,']','Fizz')
    if counter % 5 == 0:
        print('[',counter,']','Buzz')
    if counter % 3 == 0 and counter % 5 == 0:
        print('[',counter,']','FizzBuzz')
    if counter % 2 != 0:
        print('[',counter,']','Prime')

