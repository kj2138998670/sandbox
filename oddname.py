"""input a name and print alternate characters"""
def main():
    name = get_name()
    num=int(input("enter the skip value"))
    print_name(name)


def print_name(name):
    print(name[::2])


def get_name():
    name = input("enter name")
    # error check for name to be blank
    while len(name) < 1:
        name = input("enter name")
    return name


main()