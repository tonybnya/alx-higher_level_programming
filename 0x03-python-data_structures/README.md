## TASKS

0. Print a list of integers
Write a function that prints all integers of a list.

- Prototype: ```def print_list_integer(my_list=[]):```
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use ```str.format()``` to print integers

```sh
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```
