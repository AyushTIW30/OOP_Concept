### Python Class and Object Demonstrations

## Overview

This repository contains Python code demonstrating the use of classes and objects, including examples of object creation, method calls, reference variables, and basic object-oriented programming (OOP) concepts. It explores how classes can be defined, how objects can interact with each other, and how reference variables can be used to manipulate objects in memory.

## Features

1. **Class Definition and Object Creation**: Learn how to define a class with attributes and methods, and create objects of that class.
2. **Method Interaction**: Demonstrates how objects can interact with methods to perform actions, such as greeting based on attributes.
3. **Reference Variables**: Learn how reference variables work in Python, and how assigning one variable to another doesn't create a new object, but instead, both variables point to the same object in memory.
4. **Object without Reference**: Shows how objects can be created without a reference variable and demonstrates the consequences of this approach.

## Code Explanation

### 1. **Class `Person` with Method `greet`**

```python
class Person:
    def __init__(self, NAme, COuntry):
        self.name = NAme
        self.country = COuntry

    def greet(self):
        if self.country == "India":
            return "Namastey {}".format(self.name)
        else:
            return "Hello {}".format(self.name)
The Person class has two attributes: name and country.
The greet method checks the country of the person and returns a greeting in different languages based on the country.
If the country is India, it greets with "Namastey".
For other countries, it greets with "Hello".
2. Creating Objects and Calling Methods
python

P1 = Person("Ayush", "India")
p2 = Person("Danial", "England")
print(P1.greet())  # Output: Namastey Ayush
print(p2.greet())  # Output: Hello Danial
print(P1.name)     # Output: Ayush
print(p2.country)  # Output: England
P1.gender = "Male"
print(P1.gender)   # Output: Male
Objects P1 and p2 are created from the Person class with different attributes.
The greet method is called for both objects to demonstrate conditional greeting based on the country.
A new attribute gender is dynamically added to the P1 object.
3. Reference Variables in Python
python

class Person:
    def __init__(self):
        self.name = "Ayush"
        self.gender = "Male"

Person()  # OBJECT WITHOUT REFERENCE
print(Person())  # Creates an object but does not store it in a variable.
p = Person()  # OBJECT WITH REFERENCE
q = p  # BOTH POINTING TO THE SAME OBJECT
print(id(p))  # Memory address of p
print(id(q))  # Memory address of q (same as p)
print(p.name)  # Access attribute of p
print(q.name)  # Access attribute of q (same object as p)
q.name = "Ankit"  # Change attribute through q
print(p.name)  # Name of p is also changed because p and q reference the same object
This part demonstrates how reference variables work in Python.
p and q point to the same memory location, so changes to q also affect p.
Person() is also shown as an object created without a reference variable.
### 4. Commented-out Code for Class and Function
python

# class Human:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# def greet(Human):
#     print("Hi I am {} and my gender is {}".format(Human.name, Human.gender))
#     p1 = Human("Ankit", "male")
#     return p1

# p = Human("Ayush", "male")
# print(greet(p))
# x = greet(p)
# print(x.name)
# print(x.gender)
This section contains a commented-out code snippet where a class Human is defined along with a greet function.
The function prints out the name and gender of a Human object and returns a new Human object.
Usage
Clone the Repository:

bash

git clone https://github.com/AyushTIW30/OOP_Concept/blob/main/Attribute.py
Run the Code:

Open the main.py file or copy the code into your Python environment to run the examples.
Observe the outputs for various operations like object creation, method calls, and reference variable usage.
Modify the Code:

Feel free to modify the class attributes or methods to see how changes affect the object behavior.
Experiment with adding more methods or attributes to the Person class or creating additional classes.
