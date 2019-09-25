#programs:
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
################################################
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
def test():
    s= "aabbbbbddeeeccbdaaa"
    cur = s[0]
    count=1
    for each in s[1:]:
        if cur == each:
            count+=1
        else:
            if count%2:
                print (cur*count,end = '')
            cur = each
            count =1
    if count%2:
        print(cur*count)
#test()




def test():
    d={}
    s = 'abba'
    status=True
    for i in s:
        d[i] = d.get(i,0)+1
    for key,value in d.items():
        if value%2==0:
            status = True
        else:
            status =False
    print(status)
#test()

def test():
    days = {"Mon":1,"Tue":2,"Wed":3,"Thu":4,"Fri":5,"Sat":6,"Sun":7}
    count = 2
    day = days.get("Mon")+2
    counts = day%7
    for k,v in days.items():
        if v == counts:
            print(k)
#test()

def test():
    s='nitin'
    j = len(s)-1
    flag=True
    for i in s:
        if i == s[j]:
            j-=1
            flag =True
        else:
            flag = False
    print(flag)

#test()


def test2(n):
    if n==1:
        return [0]
    else:
        if n%2==0:
            return [i for i in range(n//2,0,-1)]+[-j for j in range(1,n//2+1)]
        else:
            return [i for i in range(n//2,0,-1)]+[0]+[-j for j in range(1,n//2+1)]
#print(test2(3))















