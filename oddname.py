"""input a name and print alternate characters"""
def main():
name=input("enter name")
while len(name)<1:
    name=input("enter name")
print(name[::2])
main()