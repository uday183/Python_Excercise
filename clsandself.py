#instancemethod
# class R:
#     __counter=0
#     def __init__(e):
#         R.__counter +=1
#     def check(a):
#         return R.__counter
# ss=R()
#print (R.check())

# classmethod
# class R:
#     __counter = 0
#     def __init__(uday):
#         R.__counter += 1
#     @classmethod
#     def check(opopo):
#         return R.__counter
# ss = R()
# print (ss.check())
# print (R.check())

# staticmethod
# class R:
#     __counter = 0
#     def __init__(uday):
#         R.__counter += 1
#     @staticmethod
#     def check():
#         return R.__counter
# ss = R()
# # print (ss.check())
# print (R.check())

#########################classmethod&InstanceMethod&staticMethod#######################################


# value = []
# items=[x for x in raw_input().split(',')]

# for p in items:
#     intp = int(p,2)
#     if not intp%5:
#         value.append(p)

# print ','.join(value)

#####################################################
# values=[]
# for each in range(1000,3001):
#     s= str(each)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# # print ','.join(values)
# #####################################################
# s=raw_input("Enter the value :")
# d={"D":0,"L":0}
# for c in s:
#     if c.isdigit():
#         d["D"] +=1
#     elif c.isalpha():
#         d["L"] +=1
#     else:
#         pass
#######################################################
# netAmount =0
# while True:
#     s = raw_input()
#     if not s:
#         break
#     values =s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation == "D":
#         netAmount +=amount
#     elif operation =="W":
#         netAmount -=amount
#     else:
#         pass
# print (netAmount)
##########################################################
# import re
# inp = [x for x in raw_input().split(",")]
# v=[]
# for p in inp:
#     if len(p)<6 and len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[A-Z]",p):
#         continue
#     else:
#         pass
#     if not v:
#         print ("not valid")
#     v.append(p)
# print ("".join(v))
############################################################
# from operator import itemgetter
# s = []
# while True:
#     m=raw_input()
#     if not m:
#         break
#     s.append(tuple(m.split(',')))

# print (sorted(s, key=itemgetter(0,1,2)))
#############################################################
# def NumberGen(n):
#     i=0
#     while i<n:
#         j=i
#         i +=1
#         if j%7==0:
#             yield j
# for each in NumberGen(100):
#     print (each)
#############################################################
# freq={}
# line = raw_input()
# for each in line.split():
#     freq[each]=freq.get(each,0)+1

# words =freq.keys()
# words.sort()
# for w in words:
#     print "%s:%d"%(w,freq[w])
#############################################################
def check(a):
    d={}
    for each in a:
        d[each] =d.get(each,0)+1 
    return d
# print (check('udayuuuuuuuuuuuuu'))
###############################################################
# def pintdict(n):
#     d=dict()
#     for i in range(1,n+1):
#         d[i] =i*i
#     #for (key,value) in d.items():
#     for v in d.values():
#         print (v)

# print (pintdict(20))
###############################################################
# def prilis():
#     li=[]
#     for i in range(1,20):
#         li.append(i*i)
#     return li
# print (prilis())
###############################################################
# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1


# n=int(raw_input())
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))

# print ",".join(values)

# def evenGene(n):
#     i=0
#     while i<n:
#         if i%2==0:
#             yield i
#         i+=1
# for i in evenGene("1,2,3,4,5,6,7"):
#     print (i)

# s='uday'
# y='kumar'
# print (list(set([i for i in s if i not in y])))
# print (list(set([j for j in y if j not in s])))


# def str_diff(str1,str2):
#     s=list(set(str1)^set(str2))
#     return s

# str1='uday'
# str2='kumar'
# print (str_diff(str1,str2))
##################################################################
#function inside a function
# def f():
#     def g():
#         print ('inside')
#     print ('out side')
#     g()
# f()

################################################################
#function using as parameter
# def g():
#     print ("g func calling")
# def f(fun):
#     print ("f func calling")
#     fun()
# f(g)

################################################################
#decorator eaxmples
# def decorator(func):
#     def another_fun(v1,v2):
#         print (v1-v2)
#     return another_fun

# @decorator
# def test(a,b):
#     print (a+b)

# test(3,2)

#################################################################


def myList():
    arr = [0]*10
    i=0
    while i<len(arr):
        arr[i] = i
        i +=1
    return arr
#print (myList())
################################################################
def myList1():
    arr=[0]*10
    i=0
    while True:
        arr[i] = i
        i +=1
        if i >= len(arr):
            break
    return arr

#print (myList1())
########################################################

def mySum(val):
    tot = 0
    i=0
    while i < len(val):
        tot += i
        i +=1
    return tot
print (mySum([1,2,3]))
###########################################################

#class decorator
class Deco:
    def __init__(self,f):
        self.f = f
    def __call__(self, *args, **kwargs):
        print ("calling:", self.f.__name__)
        self.f()
@Deco
def test():
    print ('testing')
#print (test())

###############################################################
#default dict attempts
from collections import defaultdict

def default():
    return 0
d=defaultdict(default)
d['name'] = 'uday'
d['place'] = 'bangalore'
d['phone']
#print (d)

d =defaultdict(lambda :9)

d['name'] = 'uday'
d['place'] = 'bangalore'
d['phone']

#print (d)
a=[('a',1),('b',2),('c',3)]

b=defaultdict(list)
for i,j in a:
    b[i].append(j)
#print (b)


name='udaykumarr'
d=defaultdict(int)
for i in name:
    print d[i]
    d[i] +=1
#print (d)

######################################################################
#generators
def my_gen(x):
    while (x>0):
        if x%2==0:
            yield 'Even'
        else:
            yield 'Odd'
        x -=1

for u in my_gen(8):
    #print (u)
    pass
def eve_sq(x):
    for i in range(x):
        if i%2==0:
            yield i**2
#print (eve_sq(9))

##########################################################################

#SingleTone

class SingleTon:

    __isinstance =None
    def __init__(self):
        if SingleTon.__isinstance !=None:
            raise Exception('This is a singleton class')
        else:
            SingleTon.__isinstance = self
    
    @staticmethod
    def get_instance():
        if SingleTon.__isinstance == None:
            SingleTon()
        return SingleTon.__isinstance

# s = SingleTon.get_instance()
# print (s)

# b = SingleTon.get_instance()
# print (b)

# c = SingleTon.get_instance()
# print (c)

#restric instase
class SingleTest:
    __isinstance =1
    def __init__(self):
        if SingleTest.__isinstance >2:
            raise Exception("not more than 2 instances....")
        else:
            SingleTest.__isinstance +=1
            SingleTest.__isinstance = SingleTest.__isinstance
# p= SingleTest()
# print (p)
# p1 = SingleTest()
# print (p1)

# p2= SingleTest()
# print (p2)

##########################################################################
#Factory Method design pattern example in Python

class Cup:
    color =""
    @staticmethod
    def getCup(cupColor):
        if (cupColor == 'red'):
            return RedCup()
        elif (cupColor == 'blue'):
            return BlueCup()
        else:
            return None

class RedCup(Cup):
    color = 'red'

class BlueCup(Cup):
    color = 'blue'

redcup = Cup.getCup("red")
#print "%s(%s)" % (redcup.color, redcup.__class__.__name__)

blueCup = Cup.getCup("blue")
#print "%s(%s)" % (blueCup.color, blueCup.__class__.__name__)

##################################################################################
#Basic Algorithms

def binary_search(arr, val):
    len_arr = len(arr)
    first_value = 0
    last_value  = len_arr - 1
    while first_value <= last_value:
        mid_value = (first_value + last_value )//2
        print (mid_value,'***m')
        if val == arr[mid_value]:
            return mid_value
        if val > arr[mid_value]:
            first_value = mid_value + 1
        else:
            last_value = mid_value -1
    if first_value > last_value:
        return None
list = [2,7,19,34,53]

#print(binary_search(list,19),'*********')
#####################################################################################
#binary search recursion
def binary_search_recursion(arr,first, last, value):
    if first> last:
        return None
    else:
        mid_value = (first+last)//2
        if value > arr[mid_value]:
            return binary_search_recursion(arr, first, mid_value + 1 ,value)
        elif value < arr[mid_value]:
            return binary_search_recursion(arr, last, mid_value - 1, value)
        else:
            return mid_value
list = [2,7,19,34,53]
#print (binary_search_recursion(list,0,5,19))

#######################################################################################

#finding all possible order of arrangements of a given set of letters
def permute(lists,v):
    if lists ==1:
        return v
    else:
        return [y+x for y in permute(1,v) for x in permute(lists-1,v)]

#print(permute(2, ["a","b","c"])) 

########################################################################################
def rotate(arr):
    l= []
    arr = arr[::-1]
    size = len(arr)
    for each in range(size//2):
        l.append(arr[each])
    for each in arr:
        if not each in l:
            l.append(each)
    print (l)
arr=[1,2,3,4,5,6,7]
#print (rotate(arr))
##########################################################################################
def leftrotate(arr,n):
    l=[]
    r=[]
    f =[]
    arrr = arr[:n]
    count = 1
    for each in range(len(arrr)):
        l.append(arrr[each])
    for each in arr:
        if not each in l:
            r.append(each)
    f = r+l
    return f
arr=[1,2,3,4,5,6,7]
#print (leftrotate(arr,2))
#right rotaion
for each in range(2):
    arr.insert(0,arr.pop())
#left rotaion
for each in range(2):
    arr.append(arr.pop(0))
    #print (arr)
###########################################################################################
def test(arr,n):
    size = len(arr)
    for i in range(n):
        arr.insert(0,arr.pop())
    return arr
ar=[1,2,3,4,5,6,7,8,9]
#print (test(ar,2))
####################################################################################
# Function which pushes all 
# zeros to end of an array. 

def pushZerotoEnd():
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    count = 0
    n=len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[count] =arr[i]
            count +=1
    while count < n:
        arr[count] = 0
        count +=1
    return arr
#print (pushZerotoEnd())
        #############or############################
def pushZeroToEnd():
    arr = [1,0,2,0,3,0,4,0,5,0]
    size = len(arr)
    count =0
    for each in range(size):
        if arr[each] !=0:
            arr[count], arr[each] = arr[each], arr[count]
            count +=1
    return arr
#print (pushZeroToEnd())

##############################################################################################
#reverse
def rev(arr):
    st_index = 0
    end_index = len(arr)-1
    while st_index < end_index:
        arr[st_index] , arr[end_index] = arr[end_index],arr[st_index]
        st_index +=1
        end_index -=1
    return arr
a=[1,2,3,4]
#print (rev(a))
##############################################################################################
#reverse number

def rev_num(a):
    st=0
    end=len(a)-1
    while st<end:
        a[st],a[end] = a[end],a[st]
        st +=1
        end -=1
    return int(''.join(a))
a='123'
#print rev_num([i for i in a])

####################################################################################################

#reverse string
def rev_num(a):
    st=0
    end=len(a)-1
    while st<end:
        a[st],a[end] = a[end],a[st]
        st +=1
        end -=1
    return str(''.join(a))
a='udaykumar'
#print rev_num([i for i in a])

####################################################################################################
#reverse str middile
def rev_middile(a):
    t=[s for s in a.split(' ')]
    print (t[0])
    for i in range(1,len(t)-1):
        print (t[i][::-1])
    print (t[len(t)-1])
a='hi how are you'
print("------------------")
#print (rev_middile(a))

####################################################################################################
#no_of_elements = int(input("Enter number of elements: "))
# l=[]
# for each in range(0,no_of_elements):
#     value = int(input("Enter Values:"))
#     l.append(value)
# print (l)
# print ('Avg of given elements',sum(l)/no_of_elements)
########################################################################################################


# data=[{'subject_master__name': 'PHY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript.pdf'},
# {'subject_master__name': 'PHY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript.pdf'},
# {'subject_master__name': 'PHY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript.pdf'},
# {'subject_master__name': 'PHY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript.pdf'},
# {'subject_master__name': 'CHEMESTRY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript_wB5brXf.pdf'},
# {'subject_master__name': 'CHEMESTRY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript_wB5brXf.pdf'},
# {'subject_master__name': 'CHEMESTRY', 'url_link': 'www.google.com', 'file_path': 'file/AnswerScript_wB5brXf.pdf'}]

data =[{
    'TotalSubjectCount': '2'
}, {
    'SubjectFlag': 'H',
    'CourseGroupID': '1',
    'StatusCheck': 'O',
    'ApplyType': 'A',
    'CourseID': '151000015',
    'CourseGroupName': 'COMMON',
    'Amount': '400.00',
    'CourseName': 'APPLIED PHYSICS-I'
}, {
    'SubjectFlag': 'H',
    'CourseGroupID': '1',
    'StatusCheck': 'O',
    'ApplyType': 'A',
    'CourseID': '151000016',
    'CourseGroupName': 'COMMON',
    'Amount': '400.00',
    'CourseName': 'APPLIED CHEMISTRY-I'
}, {
    'SubjectFlag': 'H',
    'CourseGroupID': '1',
    'StatusCheck': 'O',
    'ApplyType': 'A',
    'CourseID': '151000017',
    'CourseGroupName': 'COMMON',
    'Amount': '400.00',
    'CourseName': 'APPLIED MATHEMATICS-I'
}, {
    'SubjectFlag': 'H',
    'CourseGroupID': '1',
    'StatusCheck': 'O',
    'ApplyType': 'A',
    'CourseID': '151000018',
    'CourseGroupName': 'COMMON',
    'Amount':'400.00',
    'CourseName': 'COMMUNICATIVE ENGLISH'
}, {
    'SubjectFlag': 'H',
    'CourseGroupID': '1',
    'StatusCheck': 'O',
    'ApplyType': 'A',
    'CourseID': '151000019',
    'CourseGroupName': 'COMMON',
    'Amount':'400.00',
    'CourseName': 'INTRODUCTION TO CIVIL ENGINEERING & ENGI'
}, {
    'SubjectFlag': 'H',
    'CourseGroupID': '1',
    'StatusCheck': 'O',
    'ApplyType': 'A',
    'CourseID': '151000020',
    'CourseGroupName': 'COMMON',
    'Amount': '400.00',
    'CourseName': 'INTRODUCTION TO ELECTRICAL ENGINEERING'
}]


# print (data[1:])
dicts={}
for each in data:
    if each.get('CourseGroupName') not in dicts:
        dicts[each.get('CourseGroupName')] = {'crs_grp_name':each.get('CourseGroupName'),
                                            'sub_flag':each.get('SubjectFlag'),
                                             'st_chk':each.get('StatusCheck'),
                                             'crs_grp_id':each.get('CourseGroupID'),
                                             'sub_list':[{'amount':each.get('Amount'),'crs_id':each.get('CourseID'),
                                                            'crs_name':each.get('CourseName')
                                                        }]
                                             }
    else:
        dicts[each.get('CourseGroupName')]['sub_list'].append({'crs_id':each.get('CourseID'),'crs_name':each.get('CourseName'),
                                                                'amount':each.get('Amount')})



# print (dicts.values())


#########################################################################################################################


data=[{'SubjectFlag': 'M', 'CourseID': '110102384', 'StatusCheck': 'M', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11812-UHF & MICROWAVE'},
 {'SubjectFlag': 'M', 'CourseID': '110102385', 'StatusCheck': 'M', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11813-ELECTRONIC CIRCUIT DESIGN'}, 
 {'SubjectFlag': 'M', 'CourseID': '110102386', 'StatusCheck': 'M', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11814-COMMUNICATION NETWORK'}, 
 {'SubjectFlag': 'M', 'CourseID': '110102388', 'StatusCheck': 'M', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11816-UHF & MICROWAVE - LAB '},
  {'SubjectFlag': 'M', 'CourseID': '110102389', 'StatusCheck': 'M', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11817-ELECTRONIC CIRCUIT DESIGN - LAB'},
   {'SubjectFlag': 'E', 'CourseID': '110101639', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10639-UHF AND MICROWAVES'},
    {'SubjectFlag': 'E', 'CourseID': '110101640', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10640-ELECTRONICS CIRCUIT DESIGN'},
     {'SubjectFlag': 'E', 'CourseID': '110101641', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10641-WIRELESS COMMUNICATION'},
      {'SubjectFlag': 'E', 'CourseID': '110101642', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10642-BIOMEDICAL ENGINEERING'},
       {'SubjectFlag': 'E', 'CourseID': '110101643', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10643-DIGITAL IMAGE PROCESSING'}, 
       {'SubjectFlag': 'E', 'CourseID': '110101645', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10645-EMBEDDED AND REAL TIME SYSTEM'},
        {'SubjectFlag': 'E', 'CourseID': '110101646', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10646-SMART SENSORS'},
         {'SubjectFlag': 'E', 'CourseID': '110101647', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10647-UHF AND MICROWAVES LAB'},
          {'SubjectFlag': 'E', 'CourseID': '110101648', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10648-ELECTRONICS CIRCUIT DESIGN LAB'}, 
          {'SubjectFlag': 'E', 'CourseID': '110101649', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '10649-PROJECT AND SEMINAR'}, {'SubjectFlag': 'E', 'CourseID': '110102391', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11818-ADVANCED MICROPROCESSOR'}, {'SubjectFlag': 'E', 'CourseID': '110102392', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11819-SATELLITE COMMUNICATION'}, {'SubjectFlag': 'E', 'CourseID': '110102390', 'StatusCheck': 'O', 'Applytype': 'R', 'CourseGroupID': 1, 'CourseGroupName': 'COMMON', 'CourseName': '11821-DIGITAL IMAGE PROCESSING '}]

dicts={}
for each in data:
    if each.get('CourseGroupName') not in dicts:
        dicts[each.get('CourseGroupName')] = {'crs_grp_name':each.get('CourseGroupName'),'sub_flag':each.get('SubjectFlag'),
                                            'st_chk':each.get('StatusCheck'),'crs_grp_id':each.get('CourseGroupID'),
                                            'sub_list':[{'crs_id':each.get(''),'crs_name':each.get('CourseName')}]}
    else:
        dicts[each.get('CourseGroupName')]['sub_list'].append({'crs_id':each.get('CourseID'),'crs_name':each.get('CourseName')})
#print (dicts)



######################################################################################################################################################################################
####  factorial ######
number = 5
factorial = 1
if number < 0:
    print ('no value for below zero')
elif number ==0:
    print (1)
else:
    for each in range(1, number+1):
        factorial *=each
    #print (factorial)

####################################################################################################################################
#recursion factorial
def facts(n):
    if n ==0:
        return 1
    else:
        return n*facts(n-1)
#print (facts(4))


######################################################################################################################################
def fib (n):
    a=0
    b=1
    for each in range(2, n+1):
        c = a+b
        a = b
        b = c
    return b
#print (fib(9))

#####################################################################################################################################
