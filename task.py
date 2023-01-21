name=input('enter your name:')
id=int(input('enter the id:'))
salary=float(input('enter the amount:'))
print(f'my name is {name},id is {id} and salary is {salary}')
print('my name is {},id is {} and salary is {}'.format(name,id,salary))
print('my name is %s' %name , 'id is %d' %id , 'salary is %.1f' %salary)
print('my name is ' +str(name) ,'id is ' +str(id) ,'and ' 'salary is ' +str(salary))
a,b,c=[int(x) for x in input().split()]
sum=a+b+c
avg=sum/3
print(f'the sum is {sum} and average is {avg}')
a=5,4,6
b=sum(a)
print(b)
avg=b/3
print(avg)
r=int(input('enter the radius:'))
pi=22/7
area=pi*r*r
print('the area of circle is %.2f ' %area)
import math
r=int(input('enter the radius:'))
area=math.pi*r*2
print(area)
'''even_odd_numbers_in_if_else_for_and_while'''
a=int(input('enter the value of a:'))#10
for i in range(2,a,2):
    print(i)#2 4 6 8
for i in range(1,a,2): 
    print(i)#1 3 5 7 9
if(a%2==0):
    print(f"{a} is even number")#10 is even number
else:
    print(f'{a} is odd number')    
while(a<=10):
    print(a)#0 2 4 6 8 10
    a+=2
while(a<=10):
    print(a)#1 3 5 7 9 
    a+=2
n=int(input('enter the value:'))#5
if(n==0):print(f'you entered {n}')
elif(n%2==0):print(f'{n} is even number')
else:print(f'{n} is odd number')#5 is odd  number
n=int(input())
m=int(input())
for i in range(n,m+1):
    print(i)
for i in range(100,111,2):
    print(i)
n= int(input())
while(n<=110):
    print(n)
    n+=2  
m=[5,10,15,20,25,30,35]
print(len(m))    #7
c=0
for i in m:
    c+=1
print('no of elements present inside the list is =',c) 
'''multiplication of table'''
n=int(input())
for i in range(1,11):
    print(n,'X',i,'=',n*i)    
n=0
while(n<100):
    n+=1
    if n<0:
        continue
    print(n)

