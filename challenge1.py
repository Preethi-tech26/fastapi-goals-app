# Session 1 - June 15 2026
# Learned: variables, lists, if/else, loops, input()
'''
Normally a loop gives you each item (goal)
enumerate also gives you a counter (i) so you can number each line
The 1 means start counting from 1 instead of 0'''
name = (input("what is your name"))
print("Hello", name)
# A list of 3 things to learn
goals = ["Python", "FastAPI", "Build an API"]
#Loop through and print each one with a number
print("Here are three things I want to learn:")
for i, goal in enumerate(goals,1):
       print(i, "-",goal)