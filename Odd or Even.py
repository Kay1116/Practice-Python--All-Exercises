#Exercise 2 (and Solution)
#The exercise comes first (with a few extras if you want the extra 
# challenge or want to spend more time), followed by a discussion. 
# Enjoy!

#Ask the user for a number. Depending on whether the number is 
# even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly 
# into num, tell that to the user. If not, print a different 
# appropriate message.


num = (int(input("Enter Number: ")))

if num % 2 == 0 :
    print("Number is even\n")
elif num % 2 == 1:
    print("Number is odd\n")
elif num % 4 == 0:
    print(" Number is a mutliple of 4\n")



checker = (int(input("Enter Number(checker): ")))
if num / checker % 2 == 0:
    print("Number divdes equally")
else: 
    print("Number does not divide equally ")


