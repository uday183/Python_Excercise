lsit=['cat','rat','mat','ant']
empty=[]
for i in lsit:
    for j in i:
        empty.append(j)
#print (empty)
#======================================

a=[x for x in "".join(['cat','rat','mat','ant']) ]
#print(a)

#======================================

b=[word[i] for word in ['cat','mat','ant','rat'] for i in range(len(word))]
#print (b)

#=========================================

# n=int(raw_input("Enter number: "))

# check={True:"Not wired",False:"weird"}
# print (check[n%2==0 and (n in range(2,6)or n > 20)])


# n = int(input('Enter the number:'))
# if (n % 2) == 0: 
#     if n in range(2,5): 
#         print ('Not weird') 
#     elif n in range(6,20): 
#         print ('weird') 
#     elif n >20: 
#         print ('Not weird') 
# else: print ('weird')

uday="Mindlogix Infra Tech"
for each in uday.split():
    #print ''.join(sorted((each.lower())))
    pass

def palindram(str1):
    mid_string=len(str1)/2
    l_v=1
    flag=True
    for i in range(0,mid_string):
        if str1[i] == str1[len(str1)-l_v]:
            flag=True
            l_v+=1
        else:
            flag=False
    return flag
#print palindram("malayalam")
#print palindram("udaydasdfasd")


dict_data={'uday/n':'kumar/n','sandeep/n':'reddy/n','praveen/n':'sam/n'}
#print {k.strip('/n'):v.strip('/n') for k,v in dict_data.items()}


####sample algorithms######

def sumOfnumbers(n):
    value=0
    for each in range(1,n+1):
        value =value+ each

    return value

#print sumOfnumbers(3)

import time

def sumOfNumber(n):
    start_time=time.time()
    value=0
    for each in range(1,n+1):
        value =value+each
    end_time=time.time()
    return value,end_time-start_time

#print sumOfNumber(3)

def sums(n):
    return n*(n+1)/2

#print sums(2)
def minOfList(alist):
    min_of_the_list=alist[0]
    for each in alist:
        if each<min_of_the_list:
            min_of_the_list=each
    return min_of_the_list

#print minOfList([4,6,9,10,8,4])


def udayanagram(s1,s2):
    value=0
    match=True
    string_sort=sorted(s1)
    string_sort_1=sorted(s2)
    for each in string_sort:
        if string_sort[value] == string_sort_1[value]:
            value+=1
        else:
            match=False
    return match
#print udayanagram('uday','udya')

# def loop(l):
#     a='l'
#     for each in l:
#         if a==each:
#             continue
#             print sorted(each)
#         else:
#             print sorted(each)
# loop(['a','j','k','n','b']) 

# # Printing prices of accessories
# for index, a in enumerate(accessories,start=1):
#     print ("Accessory: %s Price: %s"\
#            %(a,prices[index+len(cars)]))

import re

cars=['Benz', 'Audi', 'Maruthi Suziki']
accessories= ['GPS Kit', 'Car repair-tool Kit']
prices={1: '500000$', 2: '569885$', 3: '4000000$', 4: '8956565$', 5: '1234$'}


#car price
#for index,c in enumerate(cars, start=1):
    #print "Car : %s , Price: %s"%(c,prices[index])

#accessories prices
#for index,a in enumerate(accessories, start=1):
    #print "Accessories :%s, Prices : %s"%(a,prices[index])


# def udaysort():
#     l=['a','a1','a5','a163','a4']
#     strings=lambda data:int(data) if data.isdigit() else data
#     split_numbers=lambda num:[strings(d) for d in re.split('([0-9]+)',num)]
#     l.sort(key=split_numbers)
#     return l
# print udaysort()

def isdigits(d):
    if d.isdigit():
        return int(d)
    else:
        return d

def numbers_split(num):

    return [isdigits(s) for s in re.split('([0-9]+)',num)]

    
def final():
    l=['a','a1','a5','a163','a4','a45','a35']
    l.sort(key=numbers_split)
    return l
#print final()
boring_news  =  ['witnesses',
                 'allegedely',
                 'new study',
                 'rebuilt',
                 'space']

xkcd = ['dudes I know',
        'kinda probably',
        'tumblr post',
        'avenge',
        'spaace']

def change_word(word):
    if word in boring_news:
        idx=boring_news.index(word)
        return xkcd[idx]
    else:
        return word
#print change_word('witnesses')

def found_match(data,target):
    count=0
    for item in data:
        if item==target:
            count +=1
    return count

print found_match([1,2,3,4,5,6,8,8],8)

def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
#print fact(3)
from datetime import datetime, timedelta, time
def date_all(date):
    today_date=datetime.now()
    if date:
        date_list=date.split('-')
        today_date=today_date.replace(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
    return today_date


date="2017-09-08"
# print date_all(date)

var=9
dicts={}
for each in range(1, var+1):
    dicts[each]=each*each
#print dicts
s="hello world and practice makes perfect and hello world again"
words=[word for word in s.split(' ')]
#print ' '.join(sorted(list(set(words))))



#identifying duplicates in a string

def iden_string(b):
    sets=set()
    for each in b: 
        if each not in sets:
            sets.add(each)
        else:
            return each

strings='kumark'

#print iden_string(strings)
#========================================================
#decorate
def welcome(string):
    def addwelcome():
        return 'welcome to'
    return addwelcome()+string


def seconfun(name):
    return name

#print welcome(seconfun('uday'))
def decorate_examp(fun):
    def welcome_msg(site):
        return "welcome to "+fun(site)
    return welcome_msg

@decorate_examp
def site(site_nam):
    return site_nam
#print site('uday kumar')
#==========================================================
#returning multiple values
class Test:
    def __init__(self):
        self.x=20
        self.y='uday'
        self.z=2.3
def tests():
    return Test()

t=tests()
#print t.x,t.y,t.z
#ex1
def fun():
    strs='uday'
    x=20
    y=5.0
    return [strs,x,y]
#print fun()
def fun():
    d={}
    d['name']='uday kumar'
    d['age']=25
    d['height']=6.1 
    return d
#print fun()
#================================================================
import subprocess
import os
def subproces():
    user_input=raw_input("Enter application name :")
    if user_input=='sublime':
        return os.popen('subl')
    else:
        return 'requested data is not available'
    #return subprocess.Popen("subl")
#print subproces()


# import speech_recognition as sr
# from gtts import gTTS
# import os
# from playsound import playsound
# from translate import Translator


# r = sr.Recognizer()
# def identity():
#     # import ipdb; ipdb.set_trace()
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)
        
#         mytext = r.recognize_google(audio)
#         print (mytext)
#         return mytext

# print identity()

import subprocess as s
import notify2
import time
from datetime import datetime
# s.call(['notify-send'])

notify2.init('notifications')
c_t=datetime.now()
hour=datetime.now().strftime('%H:%M')
if hour=='10:30':
    n = notify2.Notification('Coffee Time!!!')
    n.show()
elif hour=='13:30':
    n = notify2.Notification('Its Lunch Time!!!')
    n.show()
elif hour =='17:30':
    n = notify2.Notification("Coffee Time!!!")
    n.show()
elif hour =='18:30':
    n = notify2.Notification('Time to go Home!!!')
    n.show()
else:
    pass

class Myclass:
    __uday_hidden_cost=3000
    def add(self, increment):
        self.__uday_hidden_cost += increment
        print (self.__uday_hidden_cost)
obj=Myclass()
obj.add(2)

# print (Myclass.__uday_hidden_cost)
#print (obj._Myclass__uday_hidden_cost)
class Test:
    __test_cost=100
obj1=Test()
#print (obj1._Test__test_cost)

# def tests(data):
#     for each in data:
#         print data





def find_n_largest_numbers(lists,numbers):
    final_list=[]
    for each in range(0,numbers):
        maxs=0
        for each in range(len(lists)):
            if lists[each]>maxs:
                maxs=lists[each]
        lists.remove(maxs)
        final_list.append(maxs)
    print (final_list)



lists = [2, 6, 41, 85, 0, 3, 7, 6, 10]
numbers=3
#find_n_largest_numbers(lists,numbers)


def my_rotate(li,num):
    my_list=[]
    for each in range(len(li)-n,len(l)):
        my_list.append(li[each])
    for each in range(0,len(li)-num):
        my_list.append(li[each])
    return my_list

n=2
l= [1, 2, 3, 4, 5, 6]

# print (my_rotate(l,n))


#decorator
def my_decorate(fun):
    def inner_decorate(name):
        return "Welcome to "+ fun(name)
    return inner_decorate
@my_decorate
def names(name):
    return name
#print names('uday')




# my_input=raw_input('Enter string:' )

# if my_input.count(my_input[0]) == len(my_input):
#     print my_input[0]
# else:
#     print my_input

def first_repeat(str):
    d={}
    for each in str:
        if each in d:
            return each
        else:
            d[each]=1
    return d
# print (first_repeat('uday uday'))

# strings=raw_input('Enter your string: ')

# l=[]

for each in strings:
    if each in l:
        l.remove(each)
    l.append(each)

# print (''.join(l))




#########search list
#wordlist = ['mississippi','miss','lake','que']

# # letters = set('s')
# def search(letters):
#     for word in wordlist:
#         if set(letters) & set(word):
#             print word
# search('is')



def check_alphabet_order(word):
    for each in range(len(word)-1):
        if word[each] > word[each+1]:
            return False
        return True

# print (check_alphabet_order('abcd'))



wordlist = ['mississippi','miss','lake','que']

# def search(n):
#     for each in wordlist:
#         if set(n) & set(each):
#             print (each)


# #search('qu')
def check_alphabet_order(word):
    for each in range(len(word)-1):
        if word[each] > word[each+1]:
            return False
        return True

# #print (check_alphabet_order('abcd'))

def highest_alpha(word):
    maxx='A'
    for each in range(len(word)):

        if word[each] > maxx:
            maxx=word[each]
    return maxx
# #print (highest_alpha('udaykumar'))

def lowest_alpha(word):
    mins='z'
    for each in range(len(word)):
        if word[each] < mins:
            mins=word[each]
    return mins

# #print (lowest_alpha('udaykumar'))


def highest_number(number):
    highnum=0
    for i in number:
        if i>highnum:
            highnum=i
    return highnum
# #print (highest_number([1,2,3,4]))


def lowest_number(number):
    lownum=100
    for each in number:
        if each<lownum:
            lownum=each
    return lownum
#print (lowest_number([1,2,3,4,5,9000]))

def find_string(string , ch):
    index=0
    while index < len(string):
        if string[index] == ch:
            return string[index]
        index +=1
    
#print (find_string("udaykumar","d"))