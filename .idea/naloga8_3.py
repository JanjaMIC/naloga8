

# Homework 8.3: Calculator
print ("naloga 8.3")
print ("enter two numbers and choose an aritmetic operation ")
first = int (input("enter first number:"))
second = int (input("enter second number:"))
operacija = (input("choose operation: +,-, / or *:"))

sestevanje = first + second
odstevanje = first - second
deljenje = first / second
mnozenje = first * second


if operacija == "+":
    print (sestevanje)
if operacija == "-":
    print (odstevanje)
if operacija == "/":
    print (deljenje)
if operacija == "*":
    print (mnozenje)