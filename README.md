# PF-Assignment-first
""" 
Exercise 1: Calculate the multiplication and sum of two numbers.
Given two integer numbers, return their product only if the product is equal to or lower than
1000. Otherwise, return their sum
"""
num1=int(input("enter num1"))
num2=int(input("enter num2"))
sum=num1+num2
product=num1*num2
if(product<=1000):
    print("product",product)
else:
    print("sum",sum)
    
    """
   Exercise 2: Print the sum of the current number and the previous number.
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current
and previous numbers.
    """
    previous num = 0
    current num =1
    while previous num <= 10:
    current sum = current num + previous num
    
    
    
