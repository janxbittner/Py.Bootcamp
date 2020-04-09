# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
# To run this class enter variable = Bank("Owner name","balance")

class Bank(object):
    ''' Instances:
        owner = accound owner
        balance = accound current balance
        status = accound status
        '''
    
    status = "active"
        
    def __init__(self,owner,balance):
        '''
        Assign variable.
        '''
        
        self.owner = owner
        self.balance = int(balance)
        
    def withdrawing(self,withvalue):
        '''
        Subtracts the amount from the account
        '''
        
        self.balance = self.balance - int(withvalue)
        print(f'Current balance is {self.balance}')
        
    def depositing(self,deposit_value):
        '''
        Adds an amount from the account
        '''
        
        self.balance = self.balance + int(deposit_value)
        print(f'Current balance is {self.balance}')
        
    def info(self):
        '''
        Print info about account.
        '''
        
        print(f'{str(self.owner)} is owner of bank account. {str(self.owner)} has {str(self.balance)} money.')

# Creating class Cards with inherited from Bank class.
class Cards(Bank):
    ''' Instances:
        Card = numbers of credit cards
        '''
        
    card = 0
        
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        
    def add_card(self):
        '''
        Adds an card to the account.
        '''
        self.card +=1
        print(f'{str(self.owner)} has {str(self.card)} credit cards.')
    
    def info_card(self):
        '''
        Print info about account.
        '''
        print(self.owner,'has a accound with balance:',self.balance,'and',self.card,'credit cards.')

'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
# To run in circle area calculation in console create variable  = circle()
# Then call: variable.area() or variable.radious()


# Importing pi value from math module
from math import pi as pi_value

#Class create
class circle (object):
    ''' Istances:
        radious = circle radious
        '''
    # Create variable radious
    rad = 0
        
    def radious(self):
        '''
        The function asks to enter the radius value.
        '''
        
        self.rad = int(input("Insert radious:"))
        
    
    def area(self):
        
        '''
        The function checks if radoius is different then 0 if yes calculate area.
        If not call function  circle.radious(self).
        Finally, it prints the area value.
        '''
        
        if self.rad == 0:
            circle.radious(self)
            print(self.rad)
        
        area_value = self.rad**2*pi_value
        print(f'The area of the circle is: {round(area_value,2)}')