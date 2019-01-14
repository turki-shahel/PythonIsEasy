'''Pirple Python is Easy Course
    Homework #2 Functions
    by Turki Shahel'''

def Title(): # a function that returns a title
    return 'Python is easy'

def Artist(): # a function that returns an artist
    return 'Turki Shahel'

def Genre(): # a function that returns a genre
    return 'Pirple course'

def Choose(choice): # a functino that returns a Boolean based an input parameter
    if type(choice) == int or type(choice) == float:
        return True
    else:
        return False

print(Title())
print(Artist())
print(Genre())

print(Choose(3))
print(Choose('ok'))
print(Choose(6.0))
