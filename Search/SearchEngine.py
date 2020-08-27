import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
import multiprocessing as mp


##############################################

class searchEngine:
    # Class variables
    n_cpu = mp.cpu_count()

    def __init__(self, parallel: bool = False):
        self.parallel = parallel
        self.data = None

    @classmethod
    def makeEngine(cls, df: pd.DataFrame, parallel: bool = False):
        # This acts as an alternative constructor
        engine = cls(parallel)
        engine.fitData(df)
        return engine

    def fitData(self, df: pd.DataFrame):
        # Check if all columns is number value
        cols = df.columns
        if all([is_numeric_dtype(df[col]) for i, col in enumerate(cols)]) == False:
            raise ValueError("The passed df has none numeric dtypes. All columns must  be numeric.")
        self.data = df


##############################################
# Notes for OOP in Python
##############################################

"""


import datetime

class Employee:
    #This is the class doc page :)
    #Call by Employee.__doc__

    # Class variables
    # This value is placed on all instances
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = "_".join([first, last]) + "@gmail.com"
        self.pay = pay

        Employee.num_of_emps += 1

     # __func__ are dunder methods
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname,self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        # Returns number of characters in fullname
        return len(self.fullname)

    # allows for call like field, Employee.fullname
    @property
    def fullname(self):
        # Prints object instances first and last value.
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # @classmethod gets class as first argument, cls
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # This acts as an alternative constructor 
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Pass neither instance or class automatically
    # acts like a normal function yet, embedded in a class
    # If a method is never called within a class, make it a staticmethod
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else: return True


# Class inheritance example
class Developer(Employee):
    raise_amount = 1.10 # custom class variable compared to Employee

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay) # passes to parent class to init
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay) # passes to parent class to init
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('--> '+ emp.fullname)

# These are instances
# Each have their own location in memory
emp_1 = Employee('Corey', 'Schafer', 6000)
emp_2 = Employee('Rick', 'Nueve', 1000000)

# Test method in class, fullname()
print(emp_1.fullname)
print(emp_2.fullname)
print()

# Check class variable
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print()

# Change class variable
# Automatically changes all instances since it is associated with the class
# Class.field = ###
Employee.raise_amount = 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# View number of instances
print(Employee.num_of_emps)
print()

# Use @classmethod
Employee.set_raise_amt(1.10)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("or")
emp_1.set_raise_amt(1.15)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# Use alternative constructor
emp_3 = Employee.from_string("John-Doe-9")
print(emp_3.fullname)
print(emp_3.pay)
print()

# use staticmetod
my_date = datetime.date(2020,8,19)
print(Employee.is_workday(my_date))
print()

# View class doc
print(Employee.__doc__)

# Sub class example
dev_1 = Developer('Corey','Schafer',50000,'Python')
dev_2 = Developer('Test','Employee',60000,'GoLang')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_1.prog_lang)
print()

mgr_1 = Manager('Sue','Smith',90000,[dev_1,dev_2])
print(mgr_1.email)
mgr_1.print_employees()
mgr_1.remove_emp(dev_1)
mgr_1.print_employees()
print()

# use __str__ method
print(emp_1)
print()

# use __str__ method
print(str(emp_1))
# use __repr__ method
print(repr(emp_1))
print()

# use __str__ method
print(emp_1.__str__())
# use __repr__ method
print(emp_1.__repr__())
print()

# use dunder add method, operator overload for addition
# returns combined pay
print(emp_1+emp_2)
print()

# print len of Employee.fullname
print(len(emp_1))
print()

# call @property
print(emp_1.fullname)
print()

# call .setter
emp_1.fullname = 'Corey Ben'
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print()

# .deleter
del emp_1.fullname

"""
