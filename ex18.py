#this one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} and arg2: {arg2}")

#ok, that *args is actually pointless, we can also do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} and arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this take no arguments
def print_none():
    print("I got nothing.")

print_two("Kalpak", "Seal")
print_two_again("Kalpak", "Seal")
print_one("First !")
print_none()

