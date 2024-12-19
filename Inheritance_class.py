


# class User:
#     def __init__(self):
#         self.name = "ayush"

#     def login(self):
#         print("login")

# class Student(User):
#     def __init__(self):
#         super().__init__()
#         self.roll_no = 21

#     def enroll(self):
#         print("enrolled in the course")


# u = User()
# s = Student()
# print(s.name)
# print(s.roll_no)
# s.login()
# s.enroll()

################################################

# WHAT GET INHERITED ?
# CONSTRUCTOR
# NON PRIVATE ATTRIBUTE
# NON PRIVATE METHODS

# class Phone:
#     def __init__(self,name,price,camera):
#         print("From inside the constructor")
#         self.name = name
#         self.price = price
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     pass


# s = Smartphone("Apple",150000,"AI Based")
# s.buy()
# print(s.name,s.price,s.camera)

### IF CHILD CLASS DOES NOT HAVE A CONSTRUCTOR THEN ONLY IT WILL CALL THE PARENT CLASS CONSTRUCTOR ELSE IT WILL GO TO PARENT CLASS TO FIND A CONSTRUCTOR

#######################################################################


# class Phone:
#     def __init__(self,name,price,camera):
#         print("From inside the constructor")
#         self.name = name
#         self.price = price
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     def __init__(self, os,ram):
#         self.os = os
#         self.ram=ram
#         print("From Smartphone class")
# s = Smartphone("Androide",8)
# s.price
### HERE WE CAN SEE THAT THE CONSTRUCTOR OF PARENT CLASS IS NOT CALLED SO THE VALUE IN IT IS NIT INITIALISED AND WE CAN'T CALL IS IT WILL SHOW ERROR

#######################################################################


# class Phone:
#     def __init__(self,name,price,camera):
#         print("From inside the constructor")
#         self.name = name
#         self.__price = price
#         self.camera = camera
#     def show(self):
#         print(self.__price)

#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     def check(self):
#         print(self.__price)
#         print("From Smartphone class")
# s = Smartphone("Apple",150000,"AI Based")
# s.show()


#######################################################################



# class Parent:
#     def __init__(self,num):
#         self.__num = num

#     def get_num(self):
#         return self.__num

# class Child(Parent):
#     def show(self):
#         print("This is in a child class")


# son = Child(100)
# print(son.get_num())
# son.show()


#######################################################################




# class Parent:
#     def __init__(self,num):
#         self.__num = num

#     def get_num(self):
#         return self.__num

# class Child(Parent):
#     def __init__(self,val, num):
#         self.__val = val


#     def get_val(self):
#         return self.__val


# son = Child(100,10)
# print(son.get_num())
# print(son.get_val())

#######################################################################


##     METHOD OVERRIDING     ##

# class Phone:
#     def __init__(self,name,price,camera):
#         print("From inside the constructor")
#         self.name = name
#         self.__price = price
#         self.camera = camera
#     def show(self):
#         print(self.__price)

#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     def buy(self):
#         print("Buying a smart phone")
#         print("From Smartphone class")
# s = Smartphone("Apple",150000,"AI Based")

# s.buy()


### AGAR 2 SAME NAME KA METHOD HONGA TOH MAINLY CHILD CLASS KA RUN HOGA NA KI PARENT KA JAISA CONSTRUCTOR MAI HOTA HAI

####################    SUPER KEYWORD   ###############################

# #
# class Phone:
#     def __init__(self,name,price,camera):
#         print("From inside the Phone constructor")
#         self.name = name
#         self.__price = price
#         self.camera = camera
#     def show(self):
#         print(self.__price)

#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     def buy(self):
#         print("Buying a smart phone")
#         super().buy()
# s = Smartphone("Apple",150000,"AI Based")

# s.buy()


#################   SUPER --> CONSTRUCTOR    ##########################
#SUPER USE KAR KA PARENT KA METHOD KO ACCESS KAR SAKTE
# DONO KA CONSTRUCTOR KO ACESS KAR SAKTE
# SUPER KEYWORD SIRF CLASS KA ANDER WORK KARTA HAI
# SUPER SA ATTRIBUTE KO ACCESS NAHI KAR SAKTE

# class Phone():
#     def __init__(self,name,price,camera):
#         print("From inside the constructor")
#         self.name = name
#         self.__price = price
#         self.camera = camera
#     def get_price(self):
#         return self.__price


# class Smartphone(Phone):

#     def __init__(self, name, price, camera, os, ram):
#         print("from inside the Smartphone constructor")
#         super().__init__(name, price, camera)
#         self.os = os
#         self.ram = ram


# s = Smartphone("Apple",150000,"AI Based","Android",8)
# t = Phone("Apple",150000,"Ai")
# print(s._Phone__price)
# print(s.os)
# print(s.name)
# print(s.get_price())

# INHERITANCE SUMMARY
# # A CLASS CAN INHERIT FROM ANOTHER CLASS
# # IT IMPROVES CODE REUSE
# # CONSTRUCTOR, ATTRIBUTER, METHODS GET INHERITED TO THE CHILD CLASS
# # THE PARENT HAVE NO ACCESS TO THE CHILE CLASS
# # PRIVATE PROPERTY ARE NOT DIRECTLE ACCESSABLE BY THE CHILD CLASS
# #



# class Bank:
#     counter = 1000
#     def __init__(self,name,balance,typee):
#         self.name = name
#         self.balance = balance
#         self.typee = typee
#         self.account_No = Bank.counter
#         Bank.counter = Bank.counter+1


# class SavingAccount(Bank):
#     def __init__(self, name, balance):
#         super().__init__(name, balance, "Savings")
#     def calculate_intrest(self):
#         print(self.balance*.7)
# class CurrentAccount(Bank):
#     def __init__(self, name, balance):
#         super().__init__(name, balance, "current")
#     def calculate_intrest(self):
#         print("There is no intrest in current")

# A = SavingAccount("Ayush",3000)
# B = CurrentAccount("palak", 5000)
# A.calculate_intrest()
# B.calculate_intrest()
# print(A.account_No)
# print(B.account_No)




class Person:
    pass
class Doctor(Person):
    def __init__(self,specialization,year):
        self.__specialization = specialization
        self.__year = year
    def get_detail(self):
        print(self.__specialization,self.__year)

class Patient(Person):
    def __init__(self,ailments,Admission_date):
        self.__ailments = ailments
        self.__Admission_date = Admission_date
    def get_detail(self):
        print(self.__ailments,self.__Admission_date)


A = Doctor("Heart",5)
A.get_detail()
B = Patient("knee injuey","30/nov/2023")
B.get_detail()
print(isinstance(A,Person))

