import json

filename = 'userName.json'
name = ''

try:
    with open(filename, 'r') as r:
        name = json.load(r)
except IOError:
    print("First-time Login")
if name != "":
    print("Welcome back, " + name + "!" )
else:
    name = input("Hello! What's your name?")
    print("Welcome, " + name  + "!")
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file")