# wordlist = ['mississippi','miss','lake','que']
# '''
# def search(n):
#     for each in wordlist:
#         if set(n) & set(each):
#             print (each)


# #search('qu')
# def check_alphabet_order(word):
#     for each in range(len(word)-1):
#         if word[each] > word[each+1]:
#             return False
#         return True

# #print (check_alphabet_order('abcd'))

# def highest_alpha(word):
#     maxx='A'
#     for each in range(len(word)):

#         if word[each] > maxx:
#             maxx=word[each]
#     return maxx
# #print (highest_alpha('udaykumar'))

# def lowest_alpha(word):
#     mins='z'
#     for each in range(len(word)):
#         if word[each] < mins:
#             mins=word[each]
#     return mins

# #print (lowest_alpha('udaykumar'))


# def highest_number(number):
#     highnum=0
#     for i in number:
#         if i>highnum:
#             highnum=i
#     return highnum
# #print (highest_number([1,2,3,4]))


# def lowest_number(number):
#     lownum=100
#     for each in number:
#         if each<lownum:
#             lownum=each
#     return lownum
# #print (lowest_number([1,2,3,4,5,9000]))
# from collections import defaultdict

# def charecter_occurance_count(word):
#     d={}
#     for each in word:
#         keys=d.keys()
#         if each in keys:
#             d[each] +=1
#         else:
#             d[each]=1
#     return d
# #print (charecter_occurance_count('udaya'))
# def search_key_in_string(char,string):
#     l_o_s=len(string)
#     i=0
#     while i<l_o_s:
#         if string[i] == char:
#             return True
#         else:
#             return False
# #print search_key_in_string("a","uday")

# def search_key_in_string(char,string):
#     for i in range(len(string)):
#         if (string[i]) == char:
#             #print (string[i])
    
        
# #print search_key_in_string("a","uday")


# def remove_letter(s,n):
#     l=[]
#     for each in s:
#         if each == n:
#             s.replace(each,'')
#         #(print s)
# #print (remove_letter('uday','u'))


# class BankAccount:
#     def __init__(self,name,money):
#         self.__name= name
#         self.__balance = money

#     def deposit(self,money):
#         self.__balance +=money

#     def withdraw(self,money):
#         #print (self.__balance)
#         if self.__balance > money:
#             self.__balance -= money
#             return money
#         else:
#             return 'no funds'
#     def checkbalance(self):
#         return self.__balance


# b1 = BankAccount('tim', 400)
# # print(b1.withdraw(500))
# # b1.deposit(500)
# # print(b1.checkbalance())
# # print(b1.withdraw(800))
# # print(b1.checkbalance())

# _formats = {
#     'ymd' : '{d.year}-{d.month}-{d.day}',
#     'mdy' : '{d.month}/{d.day}/{d.year}',
#     'dmy' : '{d.day}/{d.month}/{d.year}'
# }

# class Date:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#     def __format__(self,code):
#         if code=='':
#             code='ymd'
#         fmt=_formats[code]
#         return fmt.format(d=self)
# d=Date(2018,05,06)
# #print format(d)

# '''

# class Node:
#     def __init__(self,initial_data):
#         self.data=initial_data
#         self.next=next
#     def get_data(self):
#         return self.data
#     def get_next(self):
#         return self.next
#     def set_data(self,newval):
#         self.data=newval
#     def set_next(self,new_next):
#         self.next=new_next
# class Controller:
#     def __init__(self):
#         self.head=None
#     def add_value(self,newdata):
#         temp=Node(newdata)
#         temp.set_next(self.head)
#         self.head =temp
#     def print_list(self):
#         last_node = 0
#         if self.head:
#             current=self.head
#             while current:
#                 print (current.get_data())
#                 current=current.next
#         else:
#             print ("no data")
#     def add_value_end(self, newdata):
#         temp = Node(newdata)
#         current = self.head
#         if not current:
#             self.head = temp
#             temp.set_next(current)
#         else:
#             while current:
#                 current = current.get_next()
#             current.set_next(temp)
#             temp.get_next(None)





# aa=Controller()
# aa.add_value(1)
# aa.add_value(2)
# aa.add_value(3)
# aa.add_value(4)
# #import pdb; pdb.set_trace()
# #print ("inside the list ..")

# #aa.print_list()
# data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# st=0
# end=5
# d={}
# for i in range(0,5):
#     if data[st:end]:
#         d[i]=data[st:end]
#         st=end
#         end=end+5
# #print d


# lists=[{'uday':{'fullname':'None', 'age':26, 'role':'developer'}}, {'ram':{'fullname':'mohan','age':29,'role':'developer'}}]

# def set_name(obj):
#     obj['fullname'] = 'set_name'
#     return obj

# # data=[set_name(value) for obj in lists for key,value in obj.items() if value.get('fullname',None) is 'None']
# data=[set_name(value) for obj in lists for key,value in obj.items() if value.get('fullname',None) is 'None']
# print data
