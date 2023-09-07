# Name: Donna Jang 
# Date: 9/7/23
# This program will demonstrate how to use decision statements in python.

# This program determines if a bonus should be awarded

# The main function 
def main ():
    print('Welcome to the program')
    monthlySales = getSales()   # gets sales

# THis function gets the monthly sales
def getSales():
    monthlySales = float (input('Enter the monthly sales $'))
    return monthlySales

# function call to determine bonus
def isBonus (monthlySales)
    if monthlySales >=100000:
        print "You have earned a $5000 bonus!!!"

# function call to determine day off
def dayOff (monthlySales)
    if monthlySales >=112500:
        print "All employees get one day off!!!"

# calls main
main()
