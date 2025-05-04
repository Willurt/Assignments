import random as rnd
import math

#1 funct
def random_list(n):
    lst = []
    for i in range(n):
        tal = rnd.randint(1, 100)
        lst.append(tal)
    return lst

#2 funct
def average(lst):
    sum = 0
    for i in the_list:
        sum += i
    avg = sum / len(the_list)
    return avg

#3 funct
def only_odd(lst):
    odd_list = []
    for i in the_list:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

#4 funct
def to_string(lst):
    string = ''
    for i in range(len(the_list)):
        value = lst[i]
        string += str(value)

        is_not_end = i != len(the_list) - 1
        if is_not_end:
            string += ', '
    return string

#5 funct
#Fråga efter värden A och B
#Gå igenom listan
#Om A är innan B returnera sant
#Annars falskt 
def contains(lst, a, b):
    for i in range(len(lst)):
        value = lst[i]
        if value == a:
            if lst[i + 1] == b:
                return True        
    return False

#6 funct
def has_duplicates(lst):
    lst.sort()
    for i in range(len(lst) - 1):
        value = lst[i]
        if value == lst[i + 1]:
            return True
    return False

#7 funct
def find_closest(lst, n):
    close = 0
    new_close = 0
    for i in range(len(lst)):
        value = lst[i]
        close = n - value
        
            

#Start testing!
#Ass 1
choice = int(input('Enter how many random numbers should be generated: '))
the_list = random_list(choice)
print(the_list)

#Ass 2
print(f'Average of the list: {round(average(the_list))}')

#3
print(f'The odd numbers from the list: {only_odd(the_list)}')

#4
print(to_string(the_list))

#5
contains_list = []
print('\nNew list!')
n = input('Provide some numbers to a list!: ')
numbers = n.split()
for n in numbers:
    integer = int(n)
    contains_list.append(integer)
a = int(input('Now a number that is in the list!: '))
b = int(input('And now a second number!: '))
print(f'Does {a} and {b} come in sequence? {contains(contains_list, a, b)}')

#6
print(f'Does this list contain any duplicates? {has_duplicates(contains_list)}')

#7 
closest_list = [10, 20, 30, 40]
z = 23
print(find_closest(closest_list, z))






