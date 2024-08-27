import random
from random import randint
# str
# int
# float

myswitch = bool()  # used for flags
mylist = list()   # contains duplicates; index[start:stop:step] # iteration in one string; find duplicates, sorting (default)
mytuple = tuple()  # cannot contain duplicates
dict_like = dict()  # mutable


def function_work_with_list():
    mylist = list()
    mynewlist = []
    print(f"MyList before adding a data: {mylist}")
    mylist.append("a")
    print(f"MyList after adding a data: {mylist}")

    mylist = ["a", "b", "c", "c", 1, 2, 3, 5]
    print(mylist[0:4:2])  # IndexError
    # mylist[start:stop:step]

    for each_item in mylist:
        if each_item == 2:
            print(f"Found required letter! stopping a job!: {each_item}")

    for x in range(0, 10):
        mylist.append(random.randint(0, 1000000000))

    print(mylist)









function_work_with_list()