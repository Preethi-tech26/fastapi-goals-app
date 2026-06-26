'''
Defines a function save_profile(name, age, city) that creates a dictionary from those values and writes it to a file called profile.txt
Defines a function load_profile() that reads profile.txt and prints its contents
Calls save_profile with your own info, then calls load_profile to read it back
'''
def save_profile(name, age,city):
    profile = {"name":name, "age":age, "city" :city}
    with open("profile.txt", 'w') as file:
        file.write(str(profile))
def load_profile():
    with open("profile.txt", "r") as file:
        contents = file.read()
        print(contents)
save_profile("Prith", "35", "Charlotte")

load_profile()
        
