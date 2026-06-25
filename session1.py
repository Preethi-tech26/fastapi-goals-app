print("Hello, Prith")
# --- Variables and Data Types ---
name = "Prith"
age = 40
is_learning = True

print(name)
print(age)
print(is_learning)

# --- A List ---
goals = ["Learn Python", "Build an API", "Get a new job"]
print(goals)

# --- Accessing items in a list ---
print(goals[0])   # first  
print(goals[1])   # second  
print(goals[2])   # third  

if is_learning == True:
    print("Keep going, you're doing great!")
else:
    print("Time to start learning!")

# --- A Loop ---
print("Here are your goals:")
for goal in goals:
    print("-", goal)