#We have three types of numeric data types
# 1. int
# 2. float
# 3. complex


# int - whole numbers/numbers without decimal points
# can be +ve or -ve
# can be of unlimited length

x = 100
y = -2334534

# to know the type of integer that a variable contains use the 'type()'
print(type(x)) 


a = 12.3546
b = -3.768

print(type(a))
print(type(b))

#type conversion
# converting from one data type to another

x_to_float = float(x)
print(type(x_to_float))

# create a varibale called x_to_int that contains an integer after conversion from float to int

x_to_int = int(x)
print(type(x_to_int))


#Casting
# casting in python is done using constructor functions
# 1. int() - constructs an integer number from integer, a float, a string (so long as the string is a whole number)
# 2. float() - constructs a float from an integer or a string
# 3. str()- constructs a string from a wide variety of data types
x = int(1)
print(type(x))#prints int data type
y = int(2.678)
print(type(y))#prints int data type

z = int("30")
print(type(z)) #prints int

#Assignment: Cast the above variables (x, y, z) to float and string data types

x = float(1)
print(type(x))

y = float(2.678)
print(type(y))

z = float("30")
print(type(z))


x = str(1)
print(type(x))

y = str(2.678)
print(type(y))

z = str("30")
print(type(z))

print(type(b))


x = 100
x_to_float = float(x)
print(type(x_to_float))






















