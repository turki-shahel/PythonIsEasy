'''Pirple Python Is Easy course
    homework #4 - Lists
        by Turki Shahel'''

myUniqueList = []
myLeftovers = []
def addItemToList(item):
    if(myUniqueList.__contains__(item)):
        myLeftovers.append(item)
        return False
    else:
        myUniqueList.append(item)
        return True

addItemToList('Python is Easy')
addItemToList(3.7)
addItemToList('homework #4')
addItemToList(2019)
addItemToList('January')
addItemToList('100%')

print(myUniqueList)
print(myLeftovers)

addItemToList(3.7)
addItemToList('January')
addItemToList('january')
addItemToList(2019)
addItemToList('2019')

print(myUniqueList)
print(myLeftovers)