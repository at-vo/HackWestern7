
    
dailyValue = 0
usr = input("u gud? ")
if usr.lower() == "yes" or 'y':
    print("why")
    dailyValue = 1
elif usr.lower() == "no" or 'n':
    dailyValue = 0

if dailyValue == 1:
    print("you entered yes")
elif dailyValue == 0:
    print("you entered no")

usr = input("That’s great! Tell me about it! \n")
print("your response: ",usr)
