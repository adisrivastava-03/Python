import math
a=int(input("Enter length 1: "))
b=int(input("Enter length 2: "))
c=int(input("Enter length 3: "))
s=(a+b+c)/2
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle = ",ar)

############################################
for i in range(5):
    print(i)
############################################
for i in range(5):
    print(i,end=" ")
############################################
for i in range(15):
    print("hello",end=" ")
############################################
print("\n\n")

for i in range(1,6):
    print(i,end=" ")
for i in range(4,0,-1):
############################################

for i in range(1,6):
    print( i * "* ")
############################################

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
############################################
print("\n\n")

n=int(input("Enter Row="))
for i in range(1,n+1):
    print(" "*(n-i) + "* "*(2*i-1))
############################################

n=int(input("Enter Row="))
for i in range(1,n+1):
    print("* "*i ,end="")
    for j in range(10-2*i):
        print(" ",end="")
    print("* "*i)
############################################

a=int(input("Enter 1st no.  :- "))
b=int(input("Enter 2nd no.  :- "))
print("SUM = ",a+b)
print("DIFF = ",a-b)
print("DIVIDE = ",b/a)
print("MODUOLO= ",b%a)

############################################

c=float(input("Enter the Temp in Celsius = "))
f=(c*1.8)+32
print("Fahrenhite Temp is ",f)
f=float(input("\nNow,Enter the Temp in Fahrenhite = "))
c=(f-32)/1.8
print("Celsius Temp is ",c)

############################################

year=int(input("Enter the YEAR  (yyyy) :- "))
if(year%100==0):
    if(year%400==0):
        print("LEAP YEAR")
    else:
        print("This is not LEAP YEAR")
else:
    if(year%4==0):
        print("LEAP YEAR")
    else:
        print("This is not LEAP YEAR")

############################################

A=int(input("Enter the Coefficient of x^2 i.e A :- "))
B=int(input("Enter the Coefficient of x i.e B :- "))
C=int(input("Enter the Constant i.e C :-"))
print("Quadratic Equation:- ")
print("{} x^2  +  {} x  +  {}".format(A,B,C))
d=B**2 - 4*A*C
if(d==0):
    print("Roots are Equal")
    r1=(-B+(d**0.5))/(2*A )
    r2=(-B-(d*0.5))/(2*A)
    print("Roots are :- ", r1)
    print("and ", r2)
elif(d>0):
    print("Roots are Real & Distinct")
    r1 = (-B + (d ** 0.5)) / (2 * A)
    r2 = (-B - (d * 0.5)) / (2 * A)
    print("Roots are :- ", r1)
    print("and ", r2)
else:
    print("Roots are Imaginary")

############################################

sal=int(input("Enter the Salary ;- "))
gender=input("Enter the Gender(F/M):-")
bon1=0
if(sal<10000):
    bon1=sal*(2/100)
if(gender=="M"):
    bon2=sal*(5/100)
elif(gender=="F"):
    bon2=sal*(10/100)
bonus=bon1+bon2
salary=sal+bon1+bon2
print("Total Bonus = ",bonus)
print("Total Salary = ",salary )

############################################

total=0
for i in range(5):
    marks=int(input("Enter the marks out of 100 : "))
    total+=marks
if(total>=400):
    print("GRADE  A")
elif(total>=300):
    print("GRADE  B")
elif(total>=200):
    print("GRADE  C")
else:
    print("FAIL")
############################################

x=int(input("Enter the Number: "))
n=t=x
z=l=0
while (n>0):
    l+=1
    n//=10
rem=0
while (t>0):
    rem=t%10
    z=z+rem**l
    t//=10
if(z==x):
    print("Armstrong No.\n")
else:
    print("Not Armstrong No.\n")

############################################


x=int(input("Enter the Number: "))
n=x
z=0
while (n>0):
    rem=n%10
    z=z*10+rem
    n//=10
if(x==z):
    print("Palindrome No.")
else:
    print("Not Palindrome No.")

############################################

a,b,n=int(input("Enter Start: ")),int(input("Enter End: ")),int(input("Enter the Dividing No.: "))
print("All no divisvible by {} in range {} to {} are".format(n,a,b))
for i in range(a,b+1):
    if(i%n==0):
        print(i,end=" ")

############################################

a=input("Enter the String: ")
count=0
for i in a:
    if(i=="a" or i=="A" or i=="e" or i=="E"or i=="i" or i=="I" or i=="o" or i=="u"or i=="U"):
        count+=1
print("Total Vowels = ",count)

############################################

a=input("Enter the String: ")
z=a[::-1]
if(z==a):
    print("Palindrome")
else:
    print("Not Palindrome")

a=input("Enter the String: ")
z=a.split()
l=len(z)-1

################################################
l1=[]
n1=int(input("Enter the Size of 1st list:- "))
for i in range(n1):
    l1.append(int(input("Enter Element:- ")))
l2=[]
n2=int(input("Enter the Size of 2nd list:- "))
for j in range(n2):
    l2.append(int(input("Enter Element:- ")))
l3=[]
l4=[]
l5=[]
l6=[]
print("LIST 1 :- ",l1)
print("LIST 2 :- ",l2)

############################################

l7=[]
for i in l1:
    if i not in l7:
        l7.append(i)
for i in l2:
    if i not in l7:
        l7.append(i)

############################################

print("Union :- ",l7)

for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print("Intersection :- ",l3)

for i in l1:
    if i not in l2:
        l4.append(i)
print("Difference 1-2 :- ",l4)

for j in l2:
    if j not in l1:
        l5.append(j)
print("Difference 2-1 :- ",l5)

for i in l4:
    l6.append(i)
for i in l5:
    l6.append(i)
print("Symmetric Difference :- ",l6)

#############################################
a=[]
for i in range(1,21):
    a.append(i)
print(a)
for i in a:
    if (i%2==0):
        a.pop(a.index(i))
print(a)

############################################
b=[]
for i in range(1,21):
    if(i%2==0 or i%5==0):
        b.append(i)
print(b)

############################################
