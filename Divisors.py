#Exercise 4 (and Solution)
#Create a program that asks the user for a number 
# and then prints out a list of all the divisors of that number.
#  (If you don’t know what a divisor is, it is a number that divides
#  evenly into another number. For example, 13 is 
# a divisor of 26 because 26 / 13 has no remainder.)


#user input
num = int(input("Enter number: "))

#create for loop  for num as limit for divisors
#create a array to store divisors and print
divisors =[]
for x in range(1,num):
 if num % x ==0:
  divisors.append(x)

print (divisors)
