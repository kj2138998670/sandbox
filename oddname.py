"""input a name and print alternate characters"""
def main():
name=input("enter name")
# error check for name to be blank
while len(name)<1:
    name=input("enter name")
print(name[::2])
main()