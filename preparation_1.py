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
#Threading
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
a=gen_fib(5)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

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
#import os
# my_directory = os.listdir('my_txt_files/')
# with open('uday.txt','w') as f:
#     data = 'some data to be written to the file. uday kumar'
#     f.write(data)


# with open('uday.txt','r') as f:
#     data =f.readline()
#     #print(data)

# with open(my_directory[0],'r') as f:
#     data =f.readline()
#     #print(data)

# basepath = 'my_txt_files/'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath,entry)):
#         #print(entry)
#         pass
# try:
#     os.makedirs('abdirectory/')
# except Exception as e:
#     #print(e)
#     pass

# for entry in os.listdir(basepath):
#     if entry.endswith('.txt'):
#         #print(entry)
#         pass
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

class B(T):
    def __init__(self):
        super().__init__(a=1,b=3)
    def get_parent_method(self):
        return self.get_args()

# obj = B()
# print(obj.get_parent_method())

#multi level inheritance
class A:
    def __init__(self):
        print ('calss A is Calling---A')
    def sub(self,number):
        print (number)

class B(A):
    def __init__(self):
        print ('calss B is Calling---B')
        super().__init__()
    def sub(self,number):
        print (number)
        super().sub(number+1)



class C(B):
    def __init__(self):
        print ('calss C is Calling---C')
        super().__init__()
    def sub(self,number):
        print (number)
        super().sub(number+1)

# print(C.mro())
# obj = C()
# print(obj.sub(10))


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

#print(D.mro())

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

l = [12, 45, 2, 41, 31, 10, 8, 6, 4]

h1 = l[0]
h2 = None
l1=l[0]
l2 = None
for i in l[1:]:
	if i > h1:
		h2 = h1
		h1 = i
	elif i > h2:
		h2 = i
	if i < l1:
		l2 = l1
		l1 = i
	elif l2 == None or i < l2:
		l2 =i
# print (l2)
# print (h2)

##############################################################################################################################
#Aggregation:
############################
#global interpreter log to remember django transactions 
#one class stores the reference of another class inside it.Just reference kept inside a class
class Project:
	def __init__(self,name):
		self.name = name

p1 = Project('IntelliTute')
p2 = Project('Intellicase')
p3 = Project('OSM')

class Gss:
	def __init__(self):
		self.project_list = []
	
	def add_project(self,project_obj):
		self.project_list.append(project_obj)
	
	def print_project(self):
		for proj in self.project_list:
			print(proj.name)

company = Gss()
# company.add_project(p1)
# company.add_project(p2)
# company.add_project(p3) 
# company.print_project()

##############################################################################################################################
#Compositions
############################
#one class contains object of another class
class Address:
	def __init__(self,city,state):
		self.city = city
		self.state = state
	def __str__(self):
		return ("Adress is %s - %s" % (self.city,self.state))


class Person:
	def __init__(self, name,city=None,state=None):
		self.name = name
		self.address = Address(city,state)
	def print_address(self):
		return ("Name:", self.name, "address:",self.address)

person = Person('uday','bangalore','karnataka')

#print(person.print_address())

##############################################################################################################################
#Dependency:
################
#one class object use another class temporary
class A:
	def __init__(self):
		print('dependancy')
#objA = A()

class B:
	def __init__(self):
		print('dsdsds')
	def a_class(self):
		ping = objA

##############################################################################################################################
#Association:
################
#one class object work with another class object for some amount of time.

##############################################################################################################################
#Sorting Algo:
##################
#Bubble Sort:

l = [4,3,6]
n = len(l)

for i in range(n):
	for j in range(0,n-i-1):
		if l[j] >l[j+1]:
			l[j],l[j+1] = l[j+1],l[j]

#print(l)
##############################################################################################################################
#selection sorting
l=[4,3,6]

for i in range(len(l)):
	min_value = i
	for j in range(i+1,len(l)):
		if l[min_value] > l[j]:
			min_value = j
	l[i],l[min_value] = l[min_value],l[i]
#print(l)
##############################################################################################################################
#Insertion Sort
l = [4,3,6]

def insertionSort(l):
	for index in range(1,len(l)):
		current_element = l[index]
		position = index
		while current_element < l[position-1] and position>0:
			l[position] = l[position-1]
			position = position -1
		l[position]  = current_element
	return l


#print (insertionSort(l))
##############################################################################################################################

def outer_function(func):
	def inner_function(*args):
		l = args[0]
		n = len(l)
		for i in range(n):
			for j in range(0,n-i-1):
				if l[j] > l[j+1]:
					l[j],l[j+1] = l[j+1],l[j]
		return l
	return inner_function



@outer_function
def test_sort(l):
	return l
a=[4,3,6,5]

#print(test_sort(l))
def merge(arr):
	if(len(arr) > 1):		
		mid = len(arr)//2
		l = arr[:mid]
		r=arr[mid:]

		merge(l)
		merge(r)
		i = 0
		j=0
		k=0
		while i < len(l)  and j < len(r):
			if l[i] < r[j]:
				arr[k] =l[i]
				i+=1
			else:
				arr[k] = r[j]
				j+=1
			k+=1
		while i < len(l):
			arr[k] = l[i]
			i+=1
			k+=1
		while j <len(r):
			arr[k] = r[j]
			j+=1
			k+=1
		return arr

#print merge(a)


l=[1,0,0,1,0,1]
j = 0 
for i in range(len(l)): 
	if l[i] <1: 
		j+=1 
		l[i],l[j] = l[j],l[i]

#print()
##############################################################################################################################
#Thread 
#basically python is single thread that is called "main()"
#three ways we can create the thread
#1
#functions: ---->t = Thread(target=fuction name,args) -->t.start()
#2
#Extend the thread class ---> class Mythread(Thread) --->override the run() method
#3
#without extending class ---> class Mythread: def display()----> t = Thread(target = myobj.display,args)

#Mainthread calling in python
import threading

#print("Python current Thread is :",threading.current_thread().getName())

# if threading.current_thread() == threading.main_thread():
# 	#print ('main thread is calling')
# 	pass
# else:
# 	#print('some other thread is calling')
# 	pass

################
#using functions
################
from threading import *
def printNUmbers():
	i=0
	#print('Thread Name:',threading.current_thread().getName())
	while i <= 10:
		print (i)
		i+=1
#print('Thread Name:',threading.current_thread().getName())
#t= Thread(target=printNUmbers)
#t.start()

#################
#extending class
#################
from threading import Thread
class MyThread(Thread):
	def run(self):
		i=0
		while i<=10:
			print(i)
			i+=1

#obj = MyThread()
#obj.start()


############################
#without extend thread class
#multithreading
############################
from time import sleep
class MyThread:
	def displayNumber(self):
		i=0
		print (threading.current_thread().getName())
		sleep(1)
		while i<=5:
			print(i)
			i+=1
obj = MyThread()
# t1 = Thread(target=obj.displayNumber)
# t1.start()

# t2 = Thread(target=obj.displayNumber)
# t2.start()

# t3 = Thread(target=obj.displayNumber)
# t3.start()


#Book my bus
class BookMyBus:
	def __init__(self,available_seats):
		self.available_seats=available_seats
		self.l = Lock()
	def buy(self,request_seats):
		self.l.acquire()
		print ("Number Of Seats are :",self.available_seats)
		if (self.available_seats >= request_seats):
			print("Confirming seats....")
			print("Processing Payments....")
			print("Printing Tickets........")
			self.available_seats =self.available_seats - request_seats
		else:
			print ("Sorry Seats are Not Available")
		self.l.release()
objs = BookMyBus(10)
t1 = Thread(target=objs.buy,args=(4,))
t2 = Thread(target=objs.buy,args=(4,))
t3 = Thread(target=objs.buy,args=(3,))
# t1.start()
# t2.start()
# t3.start()

#########################
#Producer and consumer
#########################

class Producer:
	def __init__(self):
		self.product_list = []
		self.status = False

	def placeing_products(self):
		for i in range(1,6):
			self.product_list.append("Product:"+str(i))
			sleep(1)
			print("Items are adding.....")
		self.status = True

class Consumer:
	def __init__(self,products):
		self.products = products

	def consumer_shipping(self):
		while self.products.status == False:
			print("waitng for the orders")
			sleep(0.2)
		print ('Orders Shipped:',self.products.product_list )

p = Producer()
c = Consumer(p)

t = Thread(target=p.placeing_products)
t1 = Thread(target = c.consumer_shipping)

# t.start()
# t1.start()

######################
#Thread Communication
######################

class Producer:
	def __init__(self):
		self.product_list = []
		self.c = Condition()

	def placeing_products(self):
		self.c.acquire()
		for i in range(1,6):
			self.product_list.append("Product:"+str(i))
			sleep(1)
			print("Items are adding.....")
		self.c.notify()
		self.c.release()

class Consumer:
	def __init__(self,products):
		self.products = products

	def consumer_shipping(self):
		self.products.c.acquire()
		self.products.c.wait(timeout=0)
		self.products.c.release()
		print ('Orders Shipped:',self.products.product_list )

p = Producer()
c = Consumer(p)

t = Thread(target=p.placeing_products)
t1 = Thread(target = c.consumer_shipping)

# t.start()
# t1.start()


class Producer:
	def __init__(self):
		self.orderList = []
		self.c = Condition()
	def addProducts(self):
		self.c.acquire()
		for i in range(1,5):
			self.orderList.append('Product:'+str(i))
			print("Adding Items.....")
		self.c.notify()
		self.c.release()

class Consumer:
	def __init__(self,prod):
		self.prod = prod

	def shipping(self):
		self.prod.c.acquire()
		self.prod.c.wait(timeout=0)
		self.prod.c.release()
		print ("Shipping Products:",self.prod.orderList)
p = Producer()
c = Consumer(p)

# t1 = Thread(target=p.addProducts())
# t2 = Thread(target=c.shipping())

# t1.start()
# t2.start()

##################################################################################################################################
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next


ll = LinkedList()
ll.head = Node(1)
second = Node(2)
thrid = Node(3)

ll.head.next = second
second.next = thrid

#print(ll.printList())

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None



class LinkedList:
	def __init__(self):
		self.head = None
	
	def push(self,new_value):
		new_data = Node(new_value)
		new_data.next = self.head
		self.head = new_data
	
	def append(self,new_value):
		new_data = Node(new_value)
		if self.head is None:
			self.head = new_data
			return
		last = self.head
		while(last.next):
			last = last.next
		last.next = new_data
	
	
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next



	def insertatnth(self, nth, value):
		self.current  = self.head
		count = 0
		while self.current:
			count += 1
			if count == nth:
				break;

			self.current= self.current.next
		obj = Node(value)
		obj.next = self.current.next
		self.current.next = obj



ll= LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.append(4)
ll.append(5)
ll.insertatnth(2,66)
print(ll.printList())

##################################################################################################################################

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
################################################
l = [3,5,6,2,3,8,9,2,1]

def sub_array_max_sum(l,size):
    new_sub = []
    for i in range(0,len(l),size):
        new_sub.append(l[i:i+size])
    print (new_sub)
    print(reduce(lambda x,y: x if sum(x)>sum(y) else y,new_sub))

#sub_array_max_sum(l,3)
################################################
s='malayalam'

def pale(s):
    for i in range(0, len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
################################################
#print(pale(s))
l=[3,6,2,1]
n=len(l)
for i in range(0,n):
    for j in range(0,n-i-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
#print (l)
################################################

def find_num1(nums,target):
    total = {}
    for i in nums:
        potentialmatch = target-i
        if potentialmatch in total:
            return [potentialmatch,i]
        else:
            total[i]=True
    print (total)

num_list=[2,3,6,11,15]
# print find_num1(num_list,9)


# import re
# p = re.compile(r'\bto\b')
# with open('uday.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         a =p.findall(line)
#         with open ('uday1.txt','w')as f:
#             f.writelines(a)

################################################
arr =[1, 0, 0, 1, 1, 0, 1]

count = 0
for i in range(len(arr)):
    if arr[i] !=0:
        arr[count] = arr[i]
        count+=1
while count < len(arr):
    arr[count] = 0
    count +=1
#print (arr)
################################################
#sum of two numbers equal to target number
l=[1,8,3,4,2,7,6]
j = len(l)-1
target = 9
for i in range(len(l)):
    if l[i]+l[j] == target:
        #print(l[i],l[j])
        j-=1
################################################

s= 'udaykumar'
d={}
for i in s:
    d[i] = d.get(i,0)+1
#print (d)
################################################
#sum of Triplets
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=10
for i in range(len(arr)-1):
    left = i+1
    right = len(arr)-1
    current = arr[i]
    while left < right:
        if current+arr[left]+arr[right] == target:
            #print(current,arr[left],arr[right])
            left +=1
            right -=1
        elif current+arr[left]+arr[right] < target:
            left +=1
        else:
            right -=1

#print (arr)

################################################
#number

l = 365
s = ''
while l>0:
    d = l%10
    s+=str(d)
    l = l//10
#print (int(s))
################################################
a=[1,1,3,4,5]
b=[2,3,6,7,8]
res =[]
for i in range(len(a)):
    if res:
        if res[-1]> a[i]:
            temp = res[-1]
            res[-1] = a[i]
            a[i] = temp
    if a[i] <= b[i]:
        res.extend((a[i],b[i]))
    else:
        res.extend((b[i]))
#print(res)


def funs():
    s= "aabbbbbddeeeccbda"
    n=s
    count = 0
    l=[]
    for i in range(len(s)-1):
        a = s[count]
        try:
            while a==s[count]:
                l.append(s[count])
                count+=1
            else:
                if len(l)%2 == 0:
                    n2 = ''.join(l)
                    n = n.replace(n2,'')
                    l=[]
                else:
                    l=[]
        except:
            print(n)
            break
#funs()









##############################################################################################################################


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
        #print(animal.make_sound())
        pass
#print (animal_sound(animals))



##################################





























































































































































##############################################################################################################################

