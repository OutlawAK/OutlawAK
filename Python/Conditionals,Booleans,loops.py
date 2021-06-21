if True:
    print("sahi hai")

# if elif else LADDER

# object identity : is


a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))

print((a is b))  # or id(a)== id(b)

a = b
print(id(a) == id(b))

# False Values:-
# False
# None
# Zero of any type
# Any empty sequence or mapping eg
# {},[],'',().

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

for i in range(1, len(a)):
    print(i, end=' - ')
print(len(a))
