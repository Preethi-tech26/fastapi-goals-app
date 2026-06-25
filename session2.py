# Session 2 - June 15 2026
# Learned: functions, dictionaries, reading/writing files

# A simple function
def greet(name):
    print("Hello", name)

# Call it
greet("Prith")
greet("Alex")

def add_numbers(a, b):
    result = a + b
    print(result)

add_numbers(5, 3)


# A dictionary
person = {
    "name": "Prith",
    "age": 35,
    "city": "Charlotte"
}

print(person)
print(person["name"])
print(person["city"])

def print_person_info(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("City:", person["city"])

print_person_info(person)
#writing to a file
with open("notes.txt", 'w') as file:
    file.write("Hello, this is my first file in Python \n")
    file.write("learning Python on weekends. \n")
    
  # Reading from a file
with open("notes.txt", "r") as file:
    contents = file.read()
    print(contents)   
    
with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())