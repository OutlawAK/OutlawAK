student = {'name': 'John', 'age': 23, 'type': ['math', 'physics']}

print(student['name'])

print(student.get('age'))

print(student.get('phone', 'not found'))
# if found sends the value, if not ,then second value is printed.

student.update({'name': 'jane', 'age': 26, 'phone': '555-5555-555'})
print(student)
# for updating

del student['age']
# for deleting any key

print(len(student))
print('                        ')
print(student.keys())  # keys
print('                        ')
print(student.values())  # values
print('                        ')
print(student.items())  # pairwise
print('                        ')

for keys, values in student.items():
    print(keys, values)
# printing thru for loop
