# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up!")

print("")

response = input("Would you like some food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")