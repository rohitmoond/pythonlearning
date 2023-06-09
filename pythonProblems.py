
# Check Even/Odd
num = int(input("Enter the number: "))
if num%2==0:
    print(num,"is Even")
else:
    print(num,"is Odd")

# Factorial
fact = 1
num = int(input("Enter a number: "))
if num <0:
    print("Please enter a non negative number")
elif num == 0:
    print("Factorial of 0 = 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of",num,"=",fact)

# Reverse & Palindrome
num = int(input("Enter the number: "))
b = num
rep = 0
while num>0:
    a = num%10
    rep = rep*10 + a
    num = num//10
print("Reverse of",b,"=",rep)
if b==rep:
    print(b,"is a Palindrome number")
else:
    print(b,"is not a Palindrome number")

# Funtions
def addition(a,b):
    print(a,'+',b,'=',a+b)
addition(5,6)
cube = lambda x:x*x*x
print(cube(7))
l1 = [1,13,56,35,77,88,90]
filter_list = list(filter(lambda x:x%2==0,l1))
print(filter_list)
map_list = list(map(lambda x: x*2,l1))
print(map_list)
from functools import reduce
reduce_list = reduce(lambda x,y : x+y,l1)
print(reduce_list)

class Employee:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def employeeDetails(self):
        print("Name of employee: ",self.name)
        print("Age of employee:",self.age)
        print("Gender of employee:",self.gender)
e1 = Employee('Rohit',27,"Male")
e1.employeeDetails()

# Roots of Quadratic Equoation
import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
D = (b*b)-(4*a*c)
if D>=0:
    r1 = (-b+(math.sqrt(D)))/(2*a)
    r2 = (-b-(math.sqrt(D)))/(2*a)
    print("Root 1 :",round(r1,2))
    print("Root 2 :",round(r2,2))
else:
    rp = -b/(2*a)
    ip = (math.sqrt(-D))/(2*a)
    print("Root 1 :",rp,"+",round(ip,2))
    print("Root 2 :",rp,"-",round(ip,2))

# Cost of House
def get_expected_cost(beds, baths):
    value = 80000+(beds*30000)+(baths*10000)
    print("House Cost with",beds,"beds and",baths,"baths =",value)

get_expected_cost(4,4)
get_expected_cost(7,3)
get_expected_cost(7,3)
get_expected_cost(7,5)

# Cost of Ring
def cost_of_ring(engraving, solid_gold):
    cost = ((not solid_gold) *(50+(len(engraving)*7))) + (solid_gold *(100+(len(engraving)*10)))
    print("Cost of ring =",cost)

cost_of_ring("Charlie+Denver", True)
cost_of_ring("08/10/2000", False)

# Cost of Water Bill
def get_water_bill(num_gallons):
    if num_gallons>=0 and num_gallons<=8000:
        bill = 5*num_gallons/1000
    elif num_gallons>=8001 and num_gallons<=22000:
        bill = 6*num_gallons/1000
    elif num_gallons>=22001 and num_gallons<=30000:
        bill = 7*num_gallons/1000
    else:
        bill = 10*num_gallons/1000
    print("Water bill for this month = Rs.",bill)

get_water_bill(7000)
get_water_bill(25000)
get_water_bill(50000)
