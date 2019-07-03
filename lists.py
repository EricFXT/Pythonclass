# Python data collection
# 1. lists - collection which is ordered and changeable, allows duplicates
# 2. tuple - is a collection which is orderd and unchangeable, allows duplicates
# 3. set - is a collection which is unordered and unindexed, no duplicates
# 4. dictionaries - is a collection which is unordered, changeable and indexed, no duplicates

# syntax for python lists
listname = ["paul", "mikey", "mary", "Laura", "Bob", "Joseph"]

#accessing items in a list
print(listname[1])
print("I am " + (listname[1]) + ".")
m = listname[1]
print("i am " + m)
print("i am {}".format(m))

#looping a list
for name in listname:
    print(name)
    print("{}".format(name))
    print(len(listname))

#checking if an item exists in a list
if "Laura" in listname:
    print("Laura is present in the list")

#syntax
# listname.append("item to be added")
#adding an item to a list at the end, use append() function
listname.append("Robert")
for name in listname:
    print(name)

# Add an item at a specific index, use insert() function
# insert() takes two arguments ;index and item name to be added
listname.insert(3, "Messi")
for name in listname:
    print(name)
#assignment
# use the following functions to the above list
# 1. remove()
# 2. pop()
# 3. del()
# 4. clear()

listname.remove("Messi")
for name in listname:
    print(name)

listname.pop(4)
for name in listname:
    print(name)
Return_value = listname.pop(4)
for name in listname:
    print(name)

listname.pop(4)
for name in listname:
    print(name)
listname.remove(1)
for name in listname:
    print(name)


