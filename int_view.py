###################################
#INDEX
#generatos and iterators
#Decorators
#lambda
#copy and deepcopy
#closures
#OOPs
#recursion
###################################

#generators and iterators:--

#generators used in functions
#it will not store the data in memory
#it gives results on fly at once means one at a time
#instead of return here we will use yield key word
#example:

#without gen
def with_out_gen(num):
    list_of_data =[]
    for i in range(num):
        d={}
        d['id'] = '1'
        d['name'] = 'uday'
        list_of_data.append(d)
    return list_of_data

#print (with_out_gen(5))

#with generator
def gen_example(num):
    for i in range(num):
        res = {"id": 1,"name":'uday'}
        yield res

#print (gen_example(10))
gen = gen_example(10)
for i in gen:
    #print (i) 
    pass

#how for loop work internal

obj = [1,2,3,4,5]
iter_obj = iter(obj)
while True:
    try:
        ele = next(iter_obj)
        #print (ele)
    except StopIteration:
        break

###################################################################################################################################
#calling function it self is called recursive function
#Recursive Functions:
def myrecurse(l):
    if not l:
        return 0
    else:
        return l[0]+myrecurse(l[1:])
l=[1,2,3,4,5]
#print (myrecurse(l))

#Arbitrary Structures
l = [1, [2, [3, 4], 5], 6, [7, 8]]

def sumtree(l):
    tot = 0
    for x in l:
        if not isinstance(x,list):
            tot +=x
        else:
            tot +=sumtree(x)
    return tot
#print (sumtree(l))
###################################################################################################################################
#myown ZIP

def myZip(*seq):
    seq = [list(s) for s in seq]
    res = []
    while all(seq):
        res.append(tuple(s.pop(0) for s in seq))
    return res

a=[1,2,3]
b=[4,5,6]
#print (myZip(a,b))

###################################################################################################################################
#First class objects

#In python functions are the first calss objects it means we can pass functions as aruguments like int,str,float.

def function1(name):
    return "Hello %s"%(name)

def print_function1(fun):
    return fun('uday')

#print (print_function1(function1))

###############################################
#Simple Decorator 

def simple_deco(func):
    def wrapper():
        print ('befor function calling')
        print (func())
        print ('after function calling')
    return wrapper

def print_name():
    return "hello uday"

obj =simple_deco(print_name)
#obj()
###############################################
#Syntactic Sugar of Decorator
#Decorators are callable objects which are used to modify functions or classes.
#Callable objects are objects which accepts some arguments and returns some objects.
#Decorators allow us to wrap another function in order to extend the behavior of wrapped function,
#without permanently modifying it.

################
#The Decorator pattern is used to dynamically add a new feature to an
# object without changing its implementation.

def simple_deco(func):
    def wrapper():
        print ('befor function calling')
        print (func())
        print ('after function calling')
    return wrapper

@simple_deco
def print_name():
    return "hello uday kumar"

#print_name()
###############################################
#args with decorator

def simple_deco(func):
    def wrapper(a,b):
       print (a-b)

    return wrapper

@simple_deco
def print_name(a,b):
    return a+b

#print_name(1,2)
###################################################################################################################################
#lambda:---
#anonymous function means that a function is without a name. 
#This function can have any number of arguments but only one expression, which is evaluated and returned.
#One is free to use lambda functions wherever function objects are required.
#Lambda definition does not include a return statement,
#it always contains an expression which is returned.

def fun(x):
    return x*x

a=lambda x: x*x

# print (fun(2))
# print (a(2))

#Lambda functions are mainly used in combination with the functions filter(), map() and reduce()
# Syntax of map:  
#map(function_object, iterable1, iterable2,...) #multiple iterables

(list(map(lambda x: x*x,[1,2,3,4])))
(list(map(lambda x,y :x+y, [1,2,3],[4,5,6] )))

#Syntax of filter:
#filter(function_object, iterable) #one iterable onle unlike map

(list(filter(lambda x: x%2==0,[1,2,3,4,5])))

#reduce:
#The function reduce(func, seq) continually applies the function func() to the sequence seq.
#It returns a single value. 
from functools import reduce

(reduce(lambda x,y:x+y,[1,2,3,4]))
#----------------------------------
f = lambda a,b: a if (a>b) else b
(reduce(f,[1,2,3,4]))

###################################################################################################################################
#shallow copy and deep copy 
#https://www.programiz.com/python-programming/shallow-deep-copy
###################################################################################################################################
#closurs
#https://www.programiz.com/python-programming/closure
###################################################################################################################################
#OOps
#basic class implementaions
class Test:
    #class attribute
    max_mrks =90
    def __init__(self,name=None):
        #instance attribute
        self.name = name
obj = Test()
obj.name = 'uday'
#access the instance attributes
#print (obj.name)
#access the class attributes
#print (obj.__class__.max_mrks)
################################################################
#creating methods in class

class Test:
    max_mrks = 90
    def __init__(self,name=None):
        self.name = name
    #class methods sample
    def printName(self):
        return self.name

obj = Test('uday')
#access the methods in a class
#print(obj.printName())
################################################################
#Inheritance
#Inheritance is a way of creating new class for using details of 
#existing class without modifying it.

class Teach:
    def __init__(self,name=None):
        self.name = 'uday'
    def printTeachName(self):
        return self.name

class Stud(Teach):
    def __init__(self,age):
        self.age = age
        super().__init__()
    def printStudName(self):
        #it takes Teach name becoz of we called super().
        return self.name

#obj = Stud(90)
# print (obj.age)
# print (obj.printStudName())

################################################################
#Encapsulation
#we can restrict access to methods and variables. 
#This prevent data from direct modification which is called encapsulation.
#In Python, we denote private attribute using underscore as prefix i.e single " _ " or double "__".

class Student:
    def __init__(self):
        self.__pass_Marks = 35
    def printPassMarks(self):
        return self.__pass_Marks
    def set_marks(self,marks):
        self.__pass_Marks = marks

obj = Student()
#print (obj.printPassMarks())

obj.__pass_Marks = 100
#it will not change the number
#print (obj.printPassMarks())

#now number will change
obj.set_marks(100)
#print (obj.printPassMarks())

################################################################
#Polymorphism
#To use common interface for multiple form (data types)
#Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). 
#However we could use same method to color any shape. This concept is called Polymorphism.

#Polymorphism of class
class WaterBottile:
    def get_color(self):
        return "RED"
class Laptop:
    def get_color(self):
        return "BLUE"

#common interface for both class

def common_interface(thing):
    return thing.get_color()

wb = WaterBottile()
lp = Laptop()

#print (common_interface(lp))

#Polymorphism of function
def sums(*args):
    return sum(args)

#print (sums(1,2,3))

################################################################
#Operator Overloading

#Operator Overloading means giving extended meaning beyond their predefined operational meaning.
#For example operator + is used to add two integers as well as join two strings and merge two lists.
#It is achievable because + operator is overloaded by int class and str class. 
#You might have noticed that the same built-in operator or function shows different behavior for objects of different classes,
# this is called Operator Overloading.

#Example class:

#print(1+2)
#print('uday')

class OperatorOverLoading(object):
    def __init__(self,a):
        self.a = a
    def __add__(self,o):
        return self.a+o.a
obj1 = OperatorOverLoading(1)
obj2 = OperatorOverLoading(1)
obj3 = OperatorOverLoading('uday')
obj4 = OperatorOverLoading('kumar')
#print (obj3+obj4)

################################################################

#Method Overloading
#Like other languages (for example method overloading in C++)
#python does not supports method overloading. 
#We may overload the methods but can only use the latest defined method.

def sum(a,b):
    return a+b

def sum(a,b,c):
    return a+b+c

#print(sum(1,2,3))

################################################################

#Single Inheritance
x=0
class Test:
    def __init__(self):
        global x
        x +=1
        #print ('class Test')

class West(Test):
    def __init__(self):
        super().__init__()
        global x
        x +=2
        #print ('class west')

#obj= West()
#print(obj())

################################################################
#Override class methods in Python
#Overriding is a very important part of OOP since it makes inheritance utilize its full power. 
#By using method overriding a class may "copy" another class, avoiding duplicated code, 
#and at the same time enhance or customize part of it. Method overriding is thus a part of the inheritance mechanism.

class Test:
    def __init__(self):
        self.value = 4
    def get_value(self):
        return self.value

class Pest(Test):
    def get_value(self):
        return self.value +1

obj = Pest()
#print (obj.get_value())
################################################################

s='abcdabcdbbaa'

def sub_string(s):
    result=[]
    dummy = []
    for idx,value in enumerate(s):
        if value in result:
            index = result.index(value)
            print (index)
            result= result[index:]
        else:
            result.append(value)
        if len(dummy) < len(result):
            dummy = result
    return len(dummy)
#print (sub_string(s))
################################################################
#sum of int
l=[]
b=65
out=0
while (b >0):
    dig = b%10
    l.append(dig)
    b=b//10
#print (l)
for each in l:
    out = out+each
#print (out)
################################################################
# number = 11
# if number > 1 :
#     for i in range(2, number//2):
#         if number%i == 0:
#             print('its not prime number')
#             break
#     else:
#         print ('its a PRIME number')
# else:
#     print ('is not prime number')
################################################################
#Calling a Method on a Parent Class
class A(object):
    def test(self):
        print('Class A is calling')

class B(A):
    def test(self):
        super(B,self).test()
        print ('Class B is calling')

obj = B()
#print (obj.test())

#multiple inheritance
# class Base:
#     def __init__(self):
#         print('Base.__init__')
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print('C.__init__')

# c=C()
#print (c)
################################################################

#Monkey Patching
#we can assign functions or method to a already established class like assing functions to a class while run time

class A(object):
    def __init__(self,num):
        self.num = num

def test(self):
    return self.num

obj = A(30)
#print (obj.num)

A.test = test

#print(obj.test())

################################################################
#adding two instance of class

class A(object):
    def __init__(self,num):
        self.num = num
    def __add__(self,obj):
        return self.num + obj.num

l = A(20)
m = A(30)
#print(l+m)

################################################################
#very imp for MRO

#Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes, including
#methods. This is known as the Method Resolution Order (MRO) 

#Python's MRO algorithm is
# 1. depth first (left to right)
# 2. No circular relationship allowed
# 3. a shared parent blocked by child

################################################################
#Duck typing about Polymorphism
#as long as classes contains same methods create comman interface for both class 
#it check calls at runtime



#Without polymorphism, a type check may be required before performing an action on an object to determine the
#correct method to call. The following counter example performs the same task as the previous code


class Pen:
    def get_color(self):
        print ('blue color')

class Car:
    def get_color(self):
        print('red color')
def comman_interface(obj):
    return obj.get_color()

p = Pen()
c = Car()

#print (comman_interface(c))

################################################################


def steps(n):
    l=[]
    l=[0]*(n+1)
    l[0:3]=[0,1,2]
    for i in range(3,n+1):
        l[i] = l[i-1]+l[i-2]
    return l[n]
#print(steps(10))


# import os
# aa=os.listdir('text/')
# for i in aa:
#     try:
#         a = i.endswith('.txt')

#         with open('/home/uday/text/'+i) as f:       
#             print (f.readline())
#     except:
#         print ('dasda')
#     else:
#         continue



################################################################
#multiple db connection
#setting .py
#DATABASE_ROUTERS = ['device_management.routers.Device2Router', 'dvs_analytics.routers.Dvs2Router','rpp_analytics.routers.RPP2Router']
######
#router.py in app

# class Dvs2Router(object):
#     """
#     A router to control all database operations on models in
#     the device_management application
#     """

#     def db_for_read(self, model, **hints):
#         """
#         Point all operations on dvs_analytics models to 'my_db_3'
#         """
#         if model._meta.app_label == 'dvs_analytics':
#             return 'DVS'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Point all operations on dvs_analytics models to 'other'
#         """
#         if model._meta.app_label == 'dvs_analytics' :
#             return 'DVS'
#         return None

#     def allow_syncdb(self, db, model):
#         """
#         Make sure the 'dvs_analytics' app only appears on the 'other' db
#         """
#         if db == 'DVS':
#             return model._meta.app_label == 'dvs_analytics'
#         elif model._meta.app_label == 'dvs_analytics':
#             return False
#         return None
        
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the auth app only appears in the 'auth_db'
#         database.
#         """
#         if app_label == 'dvs_analytics':
#             return db == 'DVS'
#         return None
################################################################

sen = "GeeksforGeeks is good to learn"

res = ' '.join(w[::-1] for w in sen.split())
# print(res,'1st stage')

def reverse(s):
    i = len(s) - 1
    sNew = ''
    while  i >= 0:
        sNew +=  s[i]
        i = i -1
    return sNew

# print (reverse(sen),'2nd stage')


s =''
for i in sen:
    s = i +s
# print (s,'3rd stage')


v = "".join(sen[i] for i in range(len(sen)-1, -1, -1))
# print (v,'4th stage')

#sub string count in a string
ini_str = "ababababa"
sub_str = 'aba'
count = 0
for i in range(len(ini_str)-1):
    sub = ini_str[i:i+3]
    if sub == sub_str:
        count +=1
# print (count)

ini_str = "abababababab"
substr = "ab"
occurence = 4
  
  
# Finding nth occurrence of substring 
inilist = [i for i in range(len(ini_str)) 
            if ini_str[i:].startswith(substr)] 


# if len(inilist)>= 4: 

#     print ("Nth occurrence of substring at", inilist[occurence-1]) 
# else: 
#     print ("No {} occurrence of substring lies in given string".format(occurence)) 
################################################################


obj = [[2,3,5,8],[2,6,7,3],[10,9,2,3]]

test_list = [j for i in obj for j in i]
# print (test_list)

original=[]
dups = []
for each in test_list:
    if each not in original:
        original.append(each)
    else:
       dups.append(each)
#print (set(dups))

################################################################
string = 'aabbbbcccaddd'
new=[]
for i in string:
    if len(new)==0:
        new.append(i)
    elif len(new) >0:
        if new[-1] == i:
            new.remove(i)
        elif new[-1]!=i:
            new.append(i)

#print (''.join(new))

################################################################
  
# s = "ILoveGeeksForGeeks"
# def readable(s):
#     print (s[0],end='')
#     i=1
#     while (i < len(s)):
#         if ( ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')):
#             print (" ", s[i].lower(), end= '')
#         else:
#             print(s[i],end='')
#         i +=1
# readable(s)

################################################################











################################################################

###################################################################################################################################


dd= {
    "1": {
        "response_status": "SB",
        "answer_status": "True",
        "txt": "<p><strong>19 + &hellip;&hellip;. = 42</strong></p>\n",
        "options": {
            "1": {
                "is_correct": "True",
                "is_select": "True",
                "txt": "<p>23</p>\n"
            },
            "2": {
                "is_correct": "False",
                "is_select": "False",
                "txt": "<p>61</p>\n"
            },
            "3": {
                "is_correct": "False",
                "is_select": "False",
                "txt": "<p>0</p>\n"
            },
            "4": {
                "is_correct": "False",
                "is_select": "False",
                "txt": "<p>42</p>\n"
            }
        }
    },
    "2": {
        "response_status": "SB",
        "answer_status": "True",
        "txt": "<p><strong>Expand the number 500428</strong></p>\n",
        "options": {
            "1": {
                "is_correct": "False",
                "is_select": "False",
                "txt": "<p>Five crore four hundred thirty eight</p>\n"
            },
            "2": {
                "is_correct": "False",
                "is_select": "False",
                "txt": "<p>fifty lakh four hundred twenty eight</p>\n"
            },
            "3": {
                "is_correct": "True",
                "is_select": "True",
                "txt": "<p>five lakh four hundred twenty eight</p>\n"
            },
            "4": {
                "is_correct": "False",
                "is_select": "False",
                "txt": "<p>five lakh four hundred eight.</p>\n"
            }
        }
    }

}

new_list = []
for data in dd:
    new = dd.get(data)
    new['inside_id'] = data
    op_list = []
    for op in dd.get(data).get('options'):
        new_op = dd.get(data).get('options').get(op)
        new_op['id'] = op
        op_list.append(new_op)
    new['options'] = op_list
    new_list.append(new)
#print(new_list)

###################################################################################################################################
#drf cache exmaples
#https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
import requests

def home(request):
    import ipdb; ipdb.set_trace()
    is_cached = ('countries' in request.session)
    if not is_cached:
        ip_address = request.META.get('REMOTE_ADDR','')
        response = requests.get('https://restcountries.eu/rest/v2/all')
        request.session['countries'] = response.json()

    countries = request.session['countries']
    request.session.set_expiry(60)
    return render(request, 'home.html', {'countries':countries})
###################################################################################################################################