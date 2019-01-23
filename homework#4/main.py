'''Pirple Python Is Easy course
    homework #4 - Lists
        by Turki Shahel'''

myUniqueList = []
rejectedList = []
def AddItemToList(item):
    if(myUniqueList.__contains__(item)):
        rejectedList.append(item)
        return False
    else:
        myUniqueList.append(item)
        return True

AddItemToList("first born")
print(myUniqueList)
AddItemToList(1)
AddItemToList("20")
print(myUniqueList)
AddItemToList(1)
print(myUniqueList)
print(rejectedList)
AddItemToList("20")
print(myUniqueList,rejectedList)