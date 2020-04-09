# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
# # Create dictionary with country and capitals
# country_and_capitals = {'Poland':'Warsaw','Germany':'Berlin','France':'Paris'} 

# # Creating a variable in which the user enters the name of the country 
# temp_country = input("Enter a country name if it exist in dictionary I show you a capital of it: ")

# # If the user entry exist in list do:
# if temp_country in country_and_capitals :
#     print(f'The capital of {temp_country.capitalize()} is {country_and_capitals[temp_country]}')

# # If the user entry not exist in list do:
# else:
#     print("Entered value don't exist in dictionares")

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
# Fibonacci_dict={}
# for i in range(1,13):
#     if i == 1:
#         Fibonacci_dict[i] = 0
#     if i == 2:
#         Fibonacci_dict[i] = 1
#     elif i > 2 :
#         Fibonacci_dict[i] = int(Fibonacci_dict[i-1]+Fibonacci_dict[i-2])
        
# print(Fibonacci_dict)

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

# companies = ["Python DS","PythonSoft","Pythazon","Pybook"]

# values = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]

# data_types = ['open','high','low',"close"]

# combined_dict ={}

# for item in range(len(data_types)):
#     combined_dict[companies[item]] = dict(zip(data_types,values[item]))

# print(combined_dict)        
      
  

'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it. PROGRAM WILL MEASURE YOUR REACTION TIME
'''
# from time import time as T
# from random import randint as rint

# _ = input("In less then 5 second after you press any value you will see START sign then press enter")

# start_time = T()
# _ = input("Press enter")
# end_time = T()
    
# print(f'Your reaction time is: {round(end_time-start_time,2)} seconds')

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
# from random import randint as rdint
# import matplotlib

# alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
# alphabet = alphabet.replace(" ","")

# alphabet_rand_dict = {}

# for char in alphabet:
#     alphabet_rand_dict[char] = rdint(1,100)

# print(alphabet_rand_dict)

# sign,val = zip(*alphabet_rand_dict.items())

# matplotlib.pyplot.bar(sign,val)
# matplotlib.pyplot.show()

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''

# suits = ['♣ Clubs','♦ Diamonds','♥ Hearts','♠ Spades']
# cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

# dict_cards = {}

# for s in suits:
#     dict_cards[s] = cards
    
# print(dict_cards)