"""
Dictionary
collection -> key+value = pair
left-side = key
right-side = value
{key1:value, key1:value}
"""
var = {'key1':100, 'key2':200}
print(var)

"""
add
update
delete
view
exit
"""
#create a dictionary
student = {
    'Prinsu':100,
    'Ayu':200
}

#Accessing an element
print(student['Prinsu']) #100
print(student['Ayu'])

#update
student['Prinsu']=300
print(student)

#delete
del student['Prinsu']
print(student)