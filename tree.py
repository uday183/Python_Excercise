number = 7
for i in range(number):
    print(' '*(number-i),end='')
    for j in range(1,i+2):
        print ('*',end='')
    for j in range(i,0,-1):
        print ('*',end='')
    print()