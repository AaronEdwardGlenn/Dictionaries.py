# we are workign with key value pairs here
student = {'name': 'Aaron', 'age': 34, 'courses': ['python', 'math']}
print(student)
print(student['name'])
print(student['courses'])

# lets look for what is not in this list properly
print(student.get('name'))
print(student.get('phone'))  # so this prints out none rather than error on us

# we can do error handling here right as the second argument of the get method
print(student.get('phone', 'not here'))

# adding to dictionary
student['phone'] = '503-555-555'
print(student)

# update the value of our object in the dictionary
student['name'] = 'Edward'
print(student)

# add and mutate values in the dictionary by using .update
student.update({'name': 'Aaron', 'age': 69, 'fave color': 'black'})
print(student)

# delete key and it's values
del student['age']
print(student)

colors = {'cool': 'blue', 'notcool': 'yellow'}

# we can also .pop to remove and also grab the values
worstColors = colors.pop('notcool')
print(colors)
print(worstColors)

# Looping through our keys and values

# How many values do we have?
print(len(student))

# print all keys or values
print(student.keys())
print(student.values())

# get a list of key and value pairs using .items()
print(student.items())

# get the keys using a for Looping
for key in student:
    print(key)

# to get the key value pairs:
for key, value in student.items():
    print(key, value)
