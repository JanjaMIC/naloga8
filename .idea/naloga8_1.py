

#Homework 8.1: The mood checker
print ("NALOGA 8.1")
x = "happy"
y = "nervous"
z = "excited"
q = "sad"
t = "relaxed"


print ("What is your mood today?" )


mood = str (input("enter your mood:"))

if mood == x :
    print ("It is great to see ya happy!")
elif mood == y :
    print ("Take a deep breath 3 times.")
elif mood == z:
    print ("Take a tea!")
elif mood == q :
    print ("Meditation can help")
elif mood == t :
    print ("That is great!")
else :
    print ("I do not recognize this mood")
