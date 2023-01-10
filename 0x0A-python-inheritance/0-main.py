#!/usr/bin/python3
lookup = __import__('0-lookup').lookup


class MyClass1(object):
    """ Class 1 """
    pass


class MyClass2(object):
    """ Class 2 """
    my_attr1 = 3

    def my_meth(self):
        """ Method doctring """
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
