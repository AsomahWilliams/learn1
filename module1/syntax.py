first = "Dave"
last = "Gray"

#print(type(first))
#print(type(first) == str)
#print(isinstance(first,str))


# constructor function
#car = str("pepperoni")
#print(type(first))
#print(type(first) == str)
#print(isinstance(car,str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# multiple lines
multiple = """
hey, how are you?

I was justchecking in.


            all good?

"""
print(multiple)

# string method
print(first)
print(first.lower())
print(first.upper())
print(first)