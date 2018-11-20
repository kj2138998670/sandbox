"""input a name and print alternate characters"""
def main():
    name = get_name()
    num=int(input("enter the skip value"))
    print_name(name,num)


def print_name(name,num):
    print(name[::num])


def get_name():
    name = input("enter name")
    # error check for name to be blank
    while len(name) < 1:
        name = input("enter name")
    return name


main()