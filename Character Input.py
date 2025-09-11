#Character Input 
#input strings types int
#Exercise 1 (and Solution)
#Create a program that asks the user to enter their 
#name and their age. Print out a message addressed to them
#that tells them the year that they will turn 100 years old.
#Note: for this exercise, the expectation is that you explicitly 
#write out the year (and therefore be out of date the next year).
#If you want to do this in a generic way, see exercise 39.

#Extras:

#Add on to the previous program by asking the user 
# for another number and printing out that many copies of the 
#m previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message 
# on separate lines. (Hint: the string "\n is 
# the same as pressing the ENTER button)


user = input("Enter your name: ").title()
age = int(input("Enter your age: "))
repeat = int(input("Enter number: "))
#calculate the year user will turn 100
year = 2025+(100- age)

#repeat message
if repeat < 0:
    print("give valid number")
else:
    for i in range(repeat):
        print(f"{user} will be 100 years old in year: {year}\n")



