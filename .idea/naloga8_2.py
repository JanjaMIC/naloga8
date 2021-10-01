# Homework 8.2: Guess the secret number
print ("NALOGA 8.2")
secret = int ("13")
print ("Guess the secet number and you are the winner!")
guess = int (input("enter your answer:"))
if secret == guess:
    print ("Congratuletions! A million is yours")
else:
    print ("Sorry!")

print ("just one chance-enter again:")
guess = int (input("enter your answer:"))
if secret == guess:
    print ("Congratuletions! A million is yours")
else:
    print ("Sorry! GAME OVER")