import string
import nltk
import numpy
    
dailyValue = 0
usr = input("u gud? ")
print(usr)
if usr.lower() == "yes" or 'y':
    print("why")
    dailyValue = 1
else:
    dailyValue = 0

if dailyValue == 1:
    print("you entered yes")
elif dailyValue == 0:
    print("you entered no")

