# Program to check eligibility to vote
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18:
    print("You are not eligible to vote!")
else:
    print("You can vote!")
