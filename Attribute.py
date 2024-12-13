class Person:
    def __init__(self,NAme , COuntry):
        self.name = NAme
        self.country = COuntry

    def greet(self):
        if self.country == "India":
            return "Namastey {}".format(self.name)
        else:
            return "Hello {}".format(self.name)



P1 = Person("Ayush","India")
p2 = Person("Danial", "England")
print(P1.greet())
print(p2.greet())
print(P1.name)
print(p2.country)
P1.gender = "Male"
print(P1.gender)
# print(p2.gender)



# REFERENCE VARIABLE:
#### Reference variable holds the object
#### We can create object without reference variable as well
#### An object can have multiple reference variable
#### Assigning a new reference variable to an existing object does not create a new object


class Person:
    def __init__(self):
        self.name = "Ayush"
        self.gender="Male"

Person() # OBJECT WITHOUT REFERENCE
print(Person())
p = Person()# OBJECT WITH REFERENCE
q= p # BOTH POINTING SAME ADDRESS
# MULTIPLE REFERENCE
print(id(p))
print(id(q))
print(p.name)
print(q.name)
q.name = "Ankit"#BOTH WERE POINTING SAME SO THE VALUE CHANGE IN Q WILL BE SAME IN P ALSO
print(p.name)


# class Human:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
# def greet(Human):
#     print( "Hi i am {} and my gender is {}".format(Human.name,Human.gender))
#     p1 = Human("ankit","male")
#     return p1

# p = Human("Ayush","male")
# print(greet(p))
# x = greet(p)
# print(x.name)
# print(x.gender)




