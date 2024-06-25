
# Class Inheritance
"""Inheritance in Python is a fundamental feature of object-oriented programming (OOP) that
allows one class (called the child or subclass) to inherit the attributes and methods
from another class (called the parent or superclass).
This enables code reusability and establishes a hierarchy between classes."""

# Key Concepts:
"""Single Inheritance: Python supports single inheritance, meaning a subclass can inherit 
from only one superclass.

Method Overriding: Subclasses can provide a specific implementation of a method 
that is already provided by its superclass. This is demonstrated with the speak method 
in Dog and Cat classes.

super() Function: Used to call the superclass’s methods and constructors.

Inheritance Hierarchy: Subclasses can further act as superclasses for other classes, 
creating a hierarchical structure.

Inheritance is powerful because it allows you to build upon existing classes, 
promoting code reuse and making the code more modular and easier to maintain."""


# In Fish class we inherit from Animal class
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
