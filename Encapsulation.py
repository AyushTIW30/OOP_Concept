#  INSTANCE VARIABLE = EK AISA VARIABLE JISKA VALUE ALAG ALAG OBJECT KA LIA ALAG ALAG HOTA HAI
from typing import Any


class Person:
    def __init__(self,name,country):
        self.name = name #SELF.NAME = INSTANCE VARIABLREE
        self.country = country # SELF.COUNTRY = INSTANCE VARIABLE


p = Person("ayush", "Germany")
print(p.name,p.country)
p2 = Person("ram","india")
print(p2.name,p2.country)

###############    ENCAPSULATION      ####################
# 1 - BASICALLY IN PYTHON WE CAN'T USE KEYWORD LIKE PRIVATE PROTECTED SO WE USE DOUBLE UNDEWRSCORE "__" IN FRONT OF THE ATTRIBUTE FPR EXAMPLE SELF.__BALANCE OR SELF.__PIN FROM NOW ONWARD WE CAN'T SEE IT IN SUGGESTIOPN BUT STILL CAN ACCESS IT BUT IT WILL NOT CHANGE THE CODE AND RUN SUCCESSFULLY


# class Atm:
#     def __init__(self ):
#         self.pin = " "
#         self.balance = 0
#         print("mai toh print ho gaya")

#         # self.menu()
#     def menu(self):
#         user_input= input("""
#             Hi how can i help you ?
#             1. press 1 to create pin
#             2. press 2 to change pin
#             3. press 3 to check balance
#             4. press 4 to withdrawl money
#             5. press anything else to exit
#             """)
#         if user_input == "1":
#             self.create_pin()
#             # create pin
#         elif user_input == "2":
#             self.change_pin()

#              # create pin
#         elif user_input == "3":
#             self.check_balance()

#             #check balance
#         elif user_input == "4":
#             self.withdrawl()
#             #withdrawl
#         else:
#             exit()
#     def create_pin(self):
#         user_pin = input("Enter the pin = ")
#         self.pin = user_pin

#         user_balance = int(input("Enter the balance = "))
#         self.balance = user_balance
#         print("pin created successfully1")
#         print(f"your  pin is {self.pin} ")
#         # next_step = int(input("Enter 1 to go to menu = "))
#         # if next_step == 1:
#         #     self.menu()
#         # else:
#         #     pass

#     def change_pin(self):
#         old_pin = input("Enter the old pin = ")
#         if old_pin == self.pin:
#             New_pin = int(input("Enter your new pin = "))
#             self.pin = New_pin
#             print("pin changed successfully")
#             print(f"Your new pin is {self.pin}")
#             next_step = int(input("Enter 1 to go to menu"))
#             if next_step == 1:
#                 self.menu()
#             else:
#                 pass
#         else:
#             print("Access not allowed")
#             next_step = input("Enter 1 to go to menu")
#             if next_step == 1:
#                 self.menu()
#             else:
#                 pass
#     def check_balance(self):
#         user_input =input("Enter the pin = ")
#         if user_input == self.pin:
#             print(f"Your current balance is {self.balance}")
#             next_step = int(input("Enter 1 to go to menu = "))
#             if next_step == 1:
#                 self.menu()
#             else:
#                 pass
#         else:
#             print("Sorry wrong pin")
#             self.menu()
#     def withdrawl(self):
#         user_input =input("Enter the pin = ")
#         if user_input == self.pin:
#             amount = int(input("Enter the amount : "))
#             if amount <= self.balance:
#                 self.balance-=amount
#                 print("withdrawl successful your current balance =",self.balance)
#             else:
#                 print("Not enough balance")
#                 next_step = int(input("Enter 1 to go to menu = "))
#                 if next_step == 1:
#                     self.menu()
#                 else:
#                    pass
#         else:
#             print("Incorrect pin sorry for inconvenience")
#             next_step = int(input("Enter 1 to go to menu = "))
#             if next_step == 1:
#                 self.menu()
#             else:
#                 pass

# obj = Atm()
# obj.create_pin()
# obj.balance = "hehehe"
# obj.withdrawl()



# AFTER ENCAPSULATION OR USING __ IN BALANCE

class Atm:

    __counter = 1


    def __init__(self ):
        self.pin = " "
        self.__balance = 0
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter+1

        print("mai toh print ho gaya")

        # self.menu()
    def get_counter(self):
        return Atm.__counter
    def set_counter(self,new_cid):
        if type(new_cid) == int:
            Atm.__counter = new_cid
        else:
            print("Not allowed")

    def get_balance(self):
        return Atm.__balance


    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Access not granted")

    def menu(self):
        user_input= input("""
            Hi how can i help you ?
            1. press 1 to create pin
            2. press 2 to change pin
            3. press 3 to check balance
            4. press 4 to withdrawl money
            5. press anything else to exit
            """)
        if user_input == "1":
            self.create_pin()
            # create pin
        elif user_input == "2":
            self.change_pin()

             # create pin
        elif user_input == "3":
            self.check_balance()

            #check balance
        elif user_input == "4":
            self.withdrawl()
            #withdrawl
        else:
            exit()
    def create_pin(self):
        user_pin = input("Enter the pin = ")
        self.pin = user_pin

        user_balance = int(input("Enter the balance = "))
        self.__balance = user_balance
        print("pin created successfully1")
        print(f"your  pin is {self.pin} ")
        # next_step = int(input("Enter 1 to go to menu = "))
        # if next_step == 1:
        #     self.menu()
        # else:
        #     pass

    def change_pin(self):
        old_pin = input("Enter the old pin = ")
        if old_pin == self.pin:
            New_pin = int(input("Enter your new pin = "))
            self.pin = New_pin
            print("pin changed successfully")
            print(f"Your new pin is {self.pin}")
            next_step = int(input("Enter 1 to go to menu"))
            if next_step == 1:
                self.menu()
            else:
                pass
        else:
            print("Access not allowed")
            next_step = input("Enter 1 to go to menu")
            if next_step == 1:
                self.menu()
            else:
                pass
    def check_balance(self):
        user_input =input("Enter the pin = ")
        if user_input == self.pin:
            print(f"Your current balance is {self.__balance}")
            next_step = int(input("Enter 1 to go to menu = "))
            if next_step == 1:
                self.menu()
            else:
                pass
        else:
            print("Sorry wrong pin")
            self.menu()
    def withdrawl(self):
        user_input =input("Enter the pin = ")
        if user_input == self.pin:
            amount = int(input("Enter the amount : "))
            if amount <= self.__balance:
                self.__balance-=amount
                print("withdrawl successful your current balance =",self.__balance)
            else:
                print("Not enough balance")
                next_step = int(input("Enter 1 to go to menu = "))
                if next_step == 1:
                    self.menu()
                else:
                   pass
        else:
            print("Incorrect pin sorry for inconvenience")
            next_step = int(input("Enter 1 to go to menu = "))
            if next_step == 1:
                self.menu()
            else:
                pass

obj = Atm()
obj1 = Atm()
obj2 = Atm()

print(obj.get_balance())

print(obj.get_counter())
print(obj1.get_counter())
print(obj2.set_counter("hehehe"))
print(obj2.get_counter())