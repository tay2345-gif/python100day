# Conditional if/else 

# > Greater than
# < Less than
# >= Greater than or Equal to
# <= Less than or Equal to
# == Equal to
# != Not equal to

print ("Welcome to the roller coaster ride !!")
bill = 0

height = int(input("What is your Height in cm ? "))
if height >= 120:
    print("You Can ride this Ride !!")
    age = int(input("What is your age ???"))
    if age < 12:
        bill = 5
        print ("Child tickets are 5$")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7$")
    elif age >= 45 and age <=55 :
        print ("Free ride on us.")
    else:
       bill = 12
       print ("Adult tickets are 12$")

       wants_photo = input("Do you want to have a photo taken ? Type y for YES n for NO")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your Final bill is {bill}")
    

    
else: 
   print("Sorry! Maybe Next time")


