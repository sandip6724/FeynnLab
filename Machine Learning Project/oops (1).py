class Person:
    #create the constructor function to define attributes
    def __init__(self,name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        
    #user defined function for Person class
    def introduce(self):
        print(f'Hi there my name is : {self.name}')
        print(f'My age is : {self.age}')
        print(f'My Gender is : {self.gender}')
        print(f'I am working as : {self.occupation}')
        
        
        
class Account:
    #Constructor function to define attribuits
    def __init__(self,Ac_no,Name,Bal):
        self.Ac_no = Ac_no
        self.Name = Name
        self.Bal = Bal
    #create a deposite function
    def deposite(self,amt):
        self.Bal = self.Bal + amt
        print(f'Amount of : {amt} INR Deposited in your Account no : {self.Ac_no}')
        print(f'Updated Balance is : {self.Bal} INR')
    #withdraw function
    def withdraw(self,amt):
        if amt <= self.Bal:
            self.Bal = self.Bal - amt
            print(f'Amount of {amt} INR is withdrawn from your Account no : {self.Ac_no}')
            print(f'Updated Balance is : {self.Bal} INR')
        else:
            print(f'Transaction declined because of Insufficent Balance')
            print(f'Current Balance is : {self.Bal} INR')
    #Transfer to another account
    def transfer(self,amt,Ac_no2):
        if amt <= self.Bal:
            self.Bal = self.Bal - amt
            Ac_no2.Bal = Ac_no2.Bal + amt
            print(f'Amount of {amt} INR transferred from your Account no : {self.Ac_no} to {Ac_no2.Ac_no}')
            print(f'Updated Balance is : {self.Bal} INR')
        else:
            print(f'Transaction declined because of Insufficent Balance')
            print(f'Current Balance is : {self.Bal} INR')
            
            
            
            
def univariate(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    # separate cat and con features
    cat = list(df.columns[df.dtypes=='object'])
    con = list(df.columns[df.dtypes!='object'])
    # Applying for loop for categural variables for countplot
    print(f'Categorical variable : {cat} countplot\n')
    for i in cat:
        plt.figure(figsize=(13,6))
        sns.countplot(data=df,x=i)
        plt.title(f'countplot for {i}')
        plt.show()
    print('\n==============================================================================================================\n')
    # apply for loop for con variable
    print(f'Contineous variable : {con} Histogram')
    for j in con:
        plt.figure(figsize=(13,6))
        sns.histplot(data=df,x=j,kde=True)
        plt.title(f'Histogram plot for {j}')
        plt.show()         
        
        
        
        
        
        
class Triangle:
    #define class attribuites to the function Triangle
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    #sides form a triangle is ((a + b) > c) and ((b + c) > a) and ((c + a) > b)
    def side(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            print('Triangle is form ')
        else:
            print('Triangle can not form ')
            
    #Perimeter of a triangle is combine of 3 sides
    def perimeter(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            print(f'Perimeter of the Triangle is : {(self.a + self.b + self.c)}')
        else:
            print("Not applicable for perimeter!")
        
    #Area of a triangle with Herons formula (s*(s-a)*(s-b)*(s-c))**(1/2)
    def area(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            s = (self.a + self.b + self.c)/2
            Ar = (s*(s - self.a)*(s - self.b)*(s - self.c))**(1/2)
            print(f'perimeter of the Triangle for Herons : {s}')
            print(f'Area of traingle with Herons : {Ar}')
        else:
            print("Not applicable for Triangle Area")
        