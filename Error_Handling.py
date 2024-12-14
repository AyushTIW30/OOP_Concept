## HERE ARE MANY ERRORS IN PYTHON
# ! -> sYNTAX ERROR = SO BY THE NAME YOU GOT ONE ERROR THAT EVERY THING IS BIG EXCEPT s SO THIS IS THE SYNTAX ERROR.......
### IT IS RAISED BY INTERPRATER
# EXAMPLE
# print"hello"


 # IT HAPENS WHEN YOU LEAVE COLON,BREAKET
 # MISSPELLING OF KEYWORD
 # INCORRECT INDENTATION
 #EMPTY IF\ELSE\ELIF\LOOP\CLASS\FUNCTION


################################################

### 2 -> IndexError

# L = [1,2,3,3]
# print(L[200])

##############################################


## 3 -> ModuleNotFoundError


# import mathsi
# math.floor(5.4)


###############################################

## 4 -> KeyError

# d = {"Name":"Ayush"}

# print(d["Age"])


##############################################

## 5 -> TypeError

# A = "i"+2
# print(A)
################################################
## 6 -> ValueError
# A = int("A")

# print(A)

################################################
## 7 -> AttributeError
# l = [1,2,3,4,5]
# l.upper

################################################
######       TRY/EXCEPT/ELSE/FINALLY


## IN TRY BLOCK WE PLACE THE PROBLEM TO CHECK
## IN EXCEPT BLOCK WE USE ALL THE EROOR SO THE THE PROGRAMMED GET EASE IN PROGRAM
## IN ELSE BLOCK WE CAN SEE THAT THE PROGRAM HAS O ERROR AND THE PROGRAM RUN VERY EASILY
## IN FINALLY BLOCK WE GET TO KNOW THAT IT WILL WORK EVEN AFTER THE ERROR RAISE


# try:
#     with open("Sample.txt","w") as f:
#         f.write("hello")
#         print(5/2)
#         print("hello")
#         l = [1,2,3,4,5]
#         l[4]
# except FileNotFoundError:
#     print("file not find")
# except NameError:
#     print("Variable not defined")
# except ZeroDivisionError:
#     print("Can't divide by 0")
# except Exception as e:
#     print(e)
# finally:
#     print("Mai toh print honga hiii samjha")



################################################

class BANK:
    def __init__(self,balance):
        self.balance = balance
    def withdrawl(self,amount):
        self.amount = amount
        if amount<0:
            raise Exception("Amount can't be -ve")
        if self.balance<amount:
            raise Exception("Paisa nahi hai tera pass")


        self.balance = self.balance-amount

obj = BANK(10000)
try:
    obj.withdrawl("hehehe")
except Exception as e:
    print(e)
else:
    print(obj.balance)








