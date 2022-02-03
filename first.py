'''
print("Samrudhi Patil")
print(10 +2)
L =["hello","Samrudhi", "Pooja", "Bapu"]
print(L)
print(L[2])
L.insert(2,"double")
print(L)
U=[1,2,3]
L.extend(U)
print(L)
L.append("Patil")
print(L)
L.pop(1)
print(L)
#L.clear()
#print(L)
L[1:3]=["Samrudhi", "Deepali"]
print(L)
for i in L:
    print(i)
for i in range(len(L)):
    print(i)
list1=[20,30,40,50]
list1.sort(reverse=True)
print(list1)
mytuple=("Samrudhi", "deepali")
y=list(mytuple)
y.append("great")
print(y)
y=("awsome")
print(y)
mytuple=tuple(y)
print(mytuple)
mydic={
    "brand":"Apple",
    "year":1998
    
}
print(mydic)
x=mydic.items()
print(x)
w=mydic.keys()
print(w)
a=mydic.values()
print(a)
mydic.update({"model":"queen"})
print(mydic)
for x,y in mydic.items():
   print(x,y)
dic=mydic.copy()
print(dic)
thisdic=dict(mydic)
print(thisdic)
a=50
b=40
if a>b and a!=b:
    print("a is greater")
elif a==b:
    print("a is eual to b")
else:
    print("b is smaller")
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
for i in range(1,16,2):
    print(i)
l1=["red","basket"]
l2=["blue","bag"]
for x in l1:
    for y in l2:
        print(x,y)
def countA(text):
    count=0
    for c in text:
        if c == 'a':
            count= count +1
    return count
print(countA("Hello World"))

count_all ="Hello World"
total_letter=0
total_digit=0
for c in count_all:
    if c.isdigit():
        total_digit+=1
    elif c.isalpha():
        total_letter+=1
    else:
        pass
print("Letters", total_letter)
print("Digits", total_digit)
        
def fizzbuzz(n):
    output=[]
    for num in range(1,n+1):
        if num % 15 ==0:
            output.append("Fizzbuzz")
        if num % 3 == 0:
            output.append("fizz")
        elif num % 5 ==0:
            output.append("buzz")
        elif num % 3==0 and num % 5==0:
            output.append("fizzbuzz")
        else:
            output.append(str("num"))
            
class Users:
    user_count=0
    def __init__(self,U_name):
      self.U_name=U_name
      Users.user_count +=1
u1 =Users("Sam")
u2 =Users("Sahil")
u3 =Users("Deepali")
print(Users.user_count)
print(u1)
price=149
item=345
txt="i want {} items and the price is {} dollars"
print(txt.format(item,price))


from types import LambdaType


class computer:
    def __init__(self):
        print("in init")
    def config(self):
        print("i5,16gb")
comp1=computer()
comp2=computer()
computer.config(comp1)
computer.config(comp2)
class Car:
    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"
Honda = Car("Honda City",21.4)
print(Honda.max_speed(150))

Skoda = Car("Skoda Octavia",13)
print(Skoda.max_speed(210))
class car:
    def __init__(self,name, mileage):
        self.name=name
        self.mileage=mileage
    def description(self):
            return f"The {self.name} car gives the mileage of {self.mileage}Km/l"
Honda=car(24.1,"Honda City")
print(Honda.description())
class Car:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
    def description(self):
          return f"The{self.name} car gives milage of {self.mileage}Km/l"
class BWM(car):
    pass
class Audi(car):
    def audi_desc(self):
        return f"This is the description methods of class Audi"
Obj1=BWM("BWM 7-Series",39.87)
print(Obj1.description())
Obj2=Audi("Audi A8 L",45)
print(Obj2.description())
class Fruit():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        pass
    def description(self):
        return f"The {self.name} is my favrouite fruit and price is {self.price}/Kg"
    pass
Obj1=Fruit("Mango",400)
print(Obj1.description())
class vegetable():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        pass
    def description(self):
        return f"The {self.name} my favourite vegtable and price is {self.price}/kg"
Obj2=vegetable("Potato",40)
print(Obj2.description())
class Home():
    def __init__(self,father,mother):
        self.father=father
        self.mother=mother
        pass
    def Home_method(self):
        return f"My {self.father} is my best buddy but my {self.mother} is good in teacher"
Obj1=Home("Hanmant","Deepali")
print(Obj1.Home_method())
class My_class():
        def instance_method(self):
            print("Hello! from %s " % self .__class__.__name__)
Obj1=My_class()
Obj1.instance_method()
class calculator():
    @staticmethod
    def add(x,y):
        return x+y
print( 'The sum is:', calculator.add(15,10) )
class School():
    def __init__(self,Name,Surname,Age):
        self.name=Name
        self.Surname=Surname
        self.Age=Age
        pass
    def Home_Method(self):
        print("My School Student Data")
        pass
    def School_Data(self):
        return f"My name is {self.name} and my surname is {self.Surname} and my age is {self.Age}"
Name1=School("Samrudhi","Patil",20)
Name2=School("Sahil","Patil",19)
Name3=School("Deepali","Patil",47)
print(Name1.School_Data())
print(Name2.School_Data())
print(Name3.School_Data())

def binary(n):
    l=''
    while n>1:
        l=l+str(n%2)
        n=n//2
        l+=str(n)
        print(l[::-l])
        return l
binary(1)
binary(5)
binary(10)

import turtle
wn = turtle.Screen()
wn = turtle.setup(540,508)
alex = turtle.Turtle()
alex.shape("turtle")
alex.color('red')
alex.circle(50)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(200)
alex.right(90)

class Students:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand="Hp"
            self.ram=8
        def show(self):
            print(self.brand,self.ram)
s1=Students("Samrudhi",7)         
s1.show()
lap1=s1.lap
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class B():
    def __init__(self):
        print("in B init")
        super().__init__(self)
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")
        pass
class C(A,B):
    def __init__(self):
        print("in C init")
        super().__init__()
    def feature5(self):
        print("feature 4 working")
    def feature6(self):
        print("feature 6 working")    
b1=C()

class Pycharm:
    def execute(self):
        print("compiling")
        print("runnung")
class Myeditor:
    def execute(self):
        print("spell check")
class laptop:
    def code(self,ide):
        ide.execute()       
ide=Myeditor()
lap1=laptop()
lap1.code(ide)
a=5
b=6
print(int. __add__(a,b))

class Students:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        r1=self.m1+other.m1
        r2=self.m2+other.m1
        s=Students(r1,r2)
        return s
s1=Students(45,67)
print(s1)   
class A():
    def show(self):
        print("in A show")
class B(A):
    pass
   # def show(self):
  #      print("in B show")
b1=B()
b1.show()  
for variable_1 in range(1,5,-1):
    print("executed")
grade_list = ["A+","A-","B","B+","A+","A+","A-"]
for grade in grade_list:
    if grade == "A+":
        print("TPF")
    else:
        print("Not TPF")      
number=28
for num in range(25,30):
    if(number>num):
        print(num)
    else:
        print(num)
        break
for num in 23, 45, 50, 65, 76, 90:
    if(num%5!=0):
        continue
    if(num%10==0):
        print(num, end=" ")
        continue
    if(num%3==0):
        print(num, end=" ")
for number in 10,15:
    for counter in range(1,3):
        print(number*counter, end=" ")
num1=16
num2=6
while(num1>=2):
    if(num1>num2):
        num1=num1/2
    else:
        print(num1)
        break
counter=0
while(counter<=9):
    if(counter%2==0):
        pass
    else:
        print(counter,end="")
        counter+=1
numbers_list = [98,45,60,71,90]
count = 10
for number in numbers_list:
    if number % 10 == 0:
        count -= 1
        continue
    counter = 0
    while counter < 2:
        last_digit = number % 10
        number = number // 10
        if last_digit > 4:
            count += 1
            break
        count += 1
        counter += 1
print(count)
print(numbers_list)

def Fahrenheit_1(Fahrenheit_1):
    celsius_1 = (Fahrenheit_1 - 32)  / 1.8
    return celsius_1  
print ("The %.2f degree Fahrenheit is equal to: %.2f Celsius"  
      %(Fahrenheit_1, Fahrenheit_1(45)))  
Fahrenheit_2 = int( input("Temperature value in degree Fahrenheit: " ))  
celsius_2 = (Fahrenheit_2 - 32) * 5/9  
print ("The %.2f degree Fahrenheit is equal to: %.2f Celsius"
      %(Fahrenheit_2, celsius_2))

def temperature(temp):
    celsius=(temp-32)* 5/9
    return celsius
print(temperature(10))
def Fahrenheit(temp):
    Fahrenheit=(temp * 9/5) + 32
    return Fahrenheit
print(Fahrenheit(30))

def Calculate_total_flight_ticket(no_Of_Adult,No_of_child):
    total_ticket_cost=0
    Intermidate_result=(no_Of_Adult*37550.0)+(No_of_child*(37550/3))
    service_tax=(7/100)*Intermidate_result
    Intermidate_result=service_tax + Intermidate_result
    Disscout_tax=(10/100) * Intermidate_result
    total_ticket_cost = Intermidate_result-Disscout_tax
    return total_ticket_cost
total_ticket_cost=Calculate_total_flight_ticket(5,2)
print("Total ticket cost",total_ticket_cost)
def func1():
  print("1")
  return 10
def func2():
    print("2")
    num=func1()
    return num
def fun3():
    print("3")
    num =func2()
    num=num*5
    return num
val=fun3()
print(val)

status="Valid"
ticket_status="Confirmed"
ticket_weight=42
ticket_weight_limit=30
extra_ticket_charge=0
if(status=="Valid"):
    print("Actually is valid")
if(ticket_status=="Confirmed"):
    if ticket_weight>0 and ticket_weight<=ticket_weight_limit:
        print("checking is cleared")
    elif (ticket_weight<=(ticket_weight_limit+10)):
        extra_ticket_charge=30*(ticket_weight-ticket_weight_limit)
    else:
        extra_ticket_charge=50*(ticket_weight -ticket_weight_limit)
        if (extra_ticket_charge>0):
            print("Extra charge will add", extra_ticket_charge)
            print("pay you Bill")
        else:
            print("ticket is not confirmed")
import turtle
wn = turtle.Screen()
wn = turtle.setup(540,508)
alex = turtle.Turtle()
alex.shape("turtle")
alex.color('blue')
alex.left(90)
alex.forward(100)
alex.write("you go to the wrong destination")

num1=0
num2=5
if (num1/num2==5) and (num1-num2>5):
    print("1")
    
def  display(num):
    message=""
    if num%3==0:
      print("Zip")
    if num%5==0:
      print("Zap")
    if num%3==0 and num%5==0:
          print("zoom")
    return message
message=display(5)
print(message)

def find_prod(num1,num2,num3):
    prod=0
    
    if num3 == 7:
        prod = -1
    elif num2 == 7:
        prod = num3
    elif num1 == 7:
        prod = num2*num3
    else:
        prod = num1*num2*num3
    return prod

prod=find_prod(1,5,3)
print(prod)
def from_triangle(num1,num2,num3):
    success="Triangle is formed"
    failure="Triangle is not Formed"
    if num1+num2>num3:
        if num2+num3>num1:
            if num1+num3>num2:
                print(success)
    else:
                print(failure)
Triangle=from_triangle(4,3,8)
print(Triangle)
def make_amount(no_of_one,no_of_five,rupees_to_make):
    five_needed=0
    one_needed=0
    five = int(rupees_to_make/5) 
    one_needed = rupees_to_make%5 
    five_needed = five if five <= no_of_five else no_of_five 
    if (five > no_of_five): 
        one_needed = rupees_to_make - 5 * no_of_five 
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))

make_amount(2,4,25)
'''
def gcd(m,n):
    fm=[4]
    for i in range(1,m+1):
        if (m%i) ==0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if (n%j) ==0:
            fn.append(j)
    cf = [20]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])
