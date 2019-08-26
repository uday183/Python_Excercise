#Topics Covered
#Decorator
#Iterator
#Generator
#Recursive
#lambda
#shallow copy and deep copy
#Closures
#Monkey Patching
#Duck typing
#File Operations
#Exception Handling
#Oops(super(),multilevel-Inheritance,MRO,Encapsulation,Polymorphism,Operator Overloading,Override class,Multiple inheritance)
#Classmethods Vs Staticmethods
#basic design pattrens for static methods
##############################################################################################################################
#HTTP status
#200 ok
#404 not found
#401 unautherised
#500 error
#403 forbidden
#405 method Notallowed
#502 Bad gateway
#501 Not implemented
#201 created
#202 Accepted
##############################################################################################################################
#Decorator
##############
#decorators allow us to wrap the another functions in order to extend the behavior
# of wraped function without permanently modifying it.

#The Decorator pattern is used to dynamically add a new feature to an
# object without changing its implementation.



def simple_deco(func):
    def inner_deco():
        return ('inner deco---',func())
    return inner_deco

@simple_deco
def test_deco():
    return ('test deco calling')

#print(test_deco())

#Decorator with arguments
def sum_deco(fun):
    def inner_deco(*args):
        return (args[0]-args[1])
    return inner_deco

@sum_deco
def test_sum_deco(a,b):
    return a+b

#print(test_sum_deco(4,6))
##############################################################################################################################
#Iterator
##############

#Iterator is a object which will return data, one element at a time.
#It is combination of two methods . 1)__iter__(), 2) __next__()
# a=[1,2,3,4]
# iters = iter(a)

# while True:
#     try:
#         ele = next(iters)
#         print (ele)
#     except StopIteration:
#         pass

##############################################################################################################################
#Generator
##############

#The difference is that, while a return statement terminates a function entirely,
#yield statement pauses the function saving all its states and later continues from there on successive calls

#Unlike normal functions, the local variables are not destroyed when the function yields.
#the generator object can be iterated only once at a time.

def gen_test():
    for i in range(5):
        yield i*2
#print (list(gen_test()))

def gen_fib(n):
    a,b = 0,1
    while a <n:
        yield a
        a,b = b,a+b
for i in gen_fib(10):
    #print (i)
    pass
a=gen_fib(10)
# print(a.next())
# print(a.next())
# print(a.next())
# print(a.next())

##############################################################################################################################
#Recursive
##############
#In Python,function can call other functions. It is even possible for the function to call itself. 
#These type of construct are termed as recursive functions.

def sum_recursive(lists):
    if not lists:
        return 0
    else:
        return lists[0]+sum_recursive(lists[1:])

#print (sum_recursive([1,2,3]))

#Arbitrary Structures
l = [1, [2, [3, 4], 5], 6, [7, 8]]

def nested_recr(lists):
    tot = 0
    for i in lists:
        if not isinstance(i,list):
            tot+=i
        else:
            tot +=nested_recr(i)
    return tot
#print(nested_recr(l))
##############################################################################################################################
#lambda
##############
#anonymous function means that a function is without a name. 
#This function can have any number of arguments but only one expression, which is evaluated and returned.
#One is free to use lambda functions wherever function objects are required.
#Lambda definition does not include a return statement,
#it always contains an expression which is returned.

#sample Example:
def f(l):
    return l*2
#print (f(2))

a = lambda x:x*2
#print (a(2))

#Lambda functions are mainly used in combination with the functions filter(), map() and reduce()
# Syntax of MAP:  
#map(function_object, iterable1, iterable2,...) #multiple iterables

a=list(map(lambda x:x*x,[1,2,3,4]))
b = list(map(lambda x,y:x+y,[1,2,3],[4,5,6]))
#print(b)

#Syntax of filter:
#filter(function_object, iterable) 
#The function is called with all the items in the list and a new list is returned 
#which contains items for which the function evaluats to True.

a= list(filter(lambda x:x%2==0,[1,2,3,4]))
#print (a)

#reduce:
#The function reduce(func, seq) continually applies the function func() to the sequence seq.
#It returns a single value. 

from functools import reduce

a = reduce(lambda x,y:x+y,[1,2,3])
#print(a)

f = lambda x,y:x if x>y else y
#print (reduce(f,[1,2,3,4]))

##############################################################################################################################
#shallow copy and deep copy
###########################

#copy:
#In Python, we use = operator to create a copy of an object. 
#You may think that this creates a new object; it doesn't. 
#It only creates a new variable that shares the reference of the original object.


#Essentially, sometimes you may want to have the original values unchanged and only modify 
#the new values or vice versa. In Python, there are two ways to create copies:Shallow Copy&Deep Copy

import copy
old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list = copy.copy(old_list)

#new list does't have reference of [5,5,5] so no changes in new list
old_list.append([5,5,5])

#new list still have reference so that changes happend in new list
old_list[1][1] = 'AAA'

# print(old_list,'old_list')
# print(new_list,'new list')

#to avoid changes is existing refence we can use deep copy
#deepcopy will not allow to changes new list

old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list = copy.deepcopy(old_list)

#new list does't have reference of [5,5,5] so no changes in new list
old_list.append([5,5,5])

#new list doesn't have any reference so that changes happend in new list
old_list[1][1] = 'AAA'

#print(old_list,'old_list')
#print(new_list,'new list')


##############################################################################################################################
#Closures
##############
#Closures can avoid the use of global values and provides some form of data hiding.
#A function defined inside another function is called a nested function. 
#Nested functions can access variables of the enclosing scope.

def print_message(msg):
    def printer():
        print (msg)
    printer()

#print (print_message('uday'))

def print_msg(msg):
    def printer():
        print(msg)
    return printer

#print(print_msg('uday'))
a = print_msg('uday')
#print(a())

#We must have a nested function (function inside a function).
#The nested function must refer to a value defined in the enclosing function.
#The enclosing function must return the nested function.

#sample example of closure
def make_multiply(num):
    def printer(value):
        return num*value
    return printer

a1 = make_multiply(2)
b1= make_multiply(3)

#print(a1(5))
#print(b1(5))
##############################################################################################################################
#Monkey Patching
#####################
#monkey patching means adding a new variable or method to a class after it's been defined. 

class B:
    def __init__(self,num):
        self.num = num

def test(self):
    return self.num

B.test = test
obj = B(30)

#print(obj.test())


#adding two instance of class
class A:
    def __init__(self,num):
        self.num = num
    def __add__(self,another_num):
        return self.num+another_num.num

obj = A(5)
obj1 = A(5)
#print (obj+obj1)

##############################################################################################################################
#Duck typing
##############

class Car:
    def get_color(self):
        print("Blue Car")

class Pen:
    def get_color(self):
        print("Pink Pen")

def comman_interface(obj):
    return obj.get_color()

c = Car()
p = Pen()

#print(comman_interface(c))
##############################################################################################################################
#Classmethods Vs Staticmethods
################################

#class method required first param as cls
#it can change the state of the class
#it can bound to class not to object
#changes reflect in all other instances

#staticmethod
#it bound to class not to object
#it can't change state of the class
#no nee to pass any class argument
#They are utility type methods that take some parameters and work upon those parameters. 
#On the other hand class methods must have class as parameter.

class A:
    value = 5
    @classmethod
    def clasmethod(cls,another_value):
        cls.value = another_value
        return cls.value

    @staticmethod
    def staticmethod():
        value = 111
        return value

# print(A.clasmethod(6))
# print(A.staticmethod())
# obj = A()
# print (obj.value)
# obj1 = A()
# print (obj1.value)

##############################################################################################################################
#File Operations
#################
import os
my_directory = os.listdir('my_txt_files/')
with open('uday.txt','w') as f:
    data = 'some data to be written to the file. uday kumar'
    f.write(data)


with open('uday.txt','r') as f:
    data =f.readline()
    #print(data)

with open(my_directory[0],'r') as f:
    data =f.readline()
    #print(data)

basepath = 'my_txt_files/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,entry)):
        #print(entry)
        pass
try:
    os.makedirs('abdirectory/')
except Exception as e:
    #print(e)
    pass

for entry in os.listdir(basepath):
    if entry.endswith('.txt'):
        #print(entry)
        pass
##############################################################################################################################
#Exception Handling
#####################
#cusomeError
class CustomError(Exception):
    pass

try:
    raise CustomError('hey this is my error class')
except  CustomError as e:
    #print ('cateched exception %s' % (e))
    pass


##############################################################################################################################
#Oops
########
#super function allows to refer superclass implicitly
#it is very usefull in multi level inheritance .super() will always refer the immediate superclass.

class T:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_args(self):
        return 'a value %s b value %s' %(self.a,self.b)

# class B(T):
#     def __init__(self):
#         super().__init__(a=1,b=3)
#     def get_parent_method(self):
#         return self.get_args()

# obj = B()
#print(obj.get_parent_method())

#multi level inheritance
class A:
    def __init__(self):
        print ('calss A is Calling---A')
    def sub(self,number):
        print (number)

# class B(A):
#     def __init__(self):
#         print ('calss B is Calling---B')
#         super().__init__()
#     def sub(self,number):
#         print (number)
#         super().sub(number+1)



# class C(B):
#     def __init__(self):
#         print ('calss C is Calling---C')
#         super().__init__()
#     def sub(self,number):
#         print (number)
#         super().sub(number+1)

# obj = C()
#print(obj.sub(10))


#very imp for MRO

#Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes, including
#methods. This is known as the Method Resolution Order (MRO) 

#Python's MRO algorithm is
# 1. depth first (left to right)
# 2. No circular relationship allowed
# 3. a shared parent blocked by child




#Encapsulation
#we can restrict access to methods and variables. 
#This prevent data from direct modification which is called encapsulation.
#In Python, we denote private attribute using underscore as prefix i.e single " _ " or double "__".

class T:
    def __init__(self):
        self.__pass_Marks = 35
    def get_pass_marks(self):
        return self.__pass_Marks
    def set_marks(self,num):
        self.__pass_Marks = num

obj =T()
#print (obj.get_pass_marks())
obj.__pass_Marks=100
#print (obj.__pass_Marks)
#print (obj.get_pass_marks())
obj.set_marks(100)
#print (obj.get_pass_marks())



#Polymorphism
#To use common interface for multiple form (data types)
#Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). 
#However we could use same method to color any shape. This concept is called Polymorphism.

class Pen:
    def get_color(self):
        print ('pen color is PINK')

class Car:
    def get_color(self):
        print ('car color is RED')

def comman_interface(obj):
    return obj.get_color()

p = Pen()
c = Car()

#print(comman_interface(c))

#Polymorphism in functions
def sums(*args):
    return sum(args)
#print sums(1,2,4)



#Operator Overloading
#For example operator + is used to add two integers as well as join two strings and merge two lists.
#It is achievable because + operator is overloaded by int class and str class. 


class OperatoOverloading:
    def __init__(self,n1):
        self.n1 = n1
    def __add__(self,n2):
        return self.n1+n2.n1
a = OperatoOverloading(1)
b = OperatoOverloading(2)
#print(a+b)

#Override class methods in Python
#method overriding a class may "copy" another class, avoiding duplicated code, 
#and at the same time enhance or customize part of it.
class Test:
    def __init__(self):
        self.value =4
    def get_value(self):
        return self.value

class Pest(Test):
    def get_value(self):
        return self.value +1

p=Pest()
#print(p.get_value())

#Multiple inheritance

class A:
    def __init__(self):
        print ('A class')

class B(A):
    def __init__(self):
        print ('B class')

class C(A):
    def __init__(self):
        print ('C class')
class D(B,C):
    def __init__(self):
        print('D class')

#if two child having same grand parent languages it will add the end
# the rule is Left -to - Right - to - Grand Parent

# print(D.mro())

##############################################################################################################################
#basic design pattrens for static methods

class Cup:
    @staticmethod
    def getcolor(color):
        if color == 'red':
            return Redcup()
        elif color == 'blue':
            return Bluecup()
        else:
            pass

class Redcup(Cup):
    color = 'red'

class Bluecup(Cup):
    color = 'blue'

#print (Cup.getcolor('red').color)

##############################################################################################################################
#programs:

a=22
b=33
c=44
def maxof(a,b,c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    return largest
#print maxof(a,b,c) 

##############################################################################################################################
#SOLID PRINCIPLES
##################

#1) Open&Close Principles

class Animal:
    def __init__(self, name):
        self.name = name
    

animals = [Animal('Lion'),Animal('Mouse')]

"""
The function animal_sound does not conform to the open-closed principle because
it cannot be closed against new kinds of animals.  If we add a new animal,
Snake, We have to modify the animal_sound function.  You see, for every new
animal, a new logic is added to the animal_sound function.  This is quite a
simple example. When your application grows and becomes complex, you will see
that the if statement would be repeated over and over again in the animal_sound
function each time a new animal is added, all over the application.
"""
def animal_sound (animals):
    for animal in animals:
        if animal.name == 'Lion':
            print('Roar')
        elif animal.name == 'Mouse':
            print('aqeak')
#print(animal_sound(animals))


class Animals:
    def __init__(self,name):
        self.name = name


class Lion(Animals):

    def make_sound(self):
        return self.name +'Make sound is: ' +'Roar'
class Snake(Animals):
    def make_sound(self):
        return self.name +'Make sound is: ' + 'HISSS'
animals = [Lion('Lion'),Snake('Snake')]

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

#print (animal_sound(animals))



##################################
#Single Responsibility Principle
##################################







##############################################################################################################################