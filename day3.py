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


#number_to_check = int(input("what is the number you want to check ? "))
#if number_to_check % 2 == 0:
#    print("Even")
#else:
 #   print("Odd")


bill = 0
print("welcome to python pizza deliveries")
size = input ("What size pizza do you want ? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N")
extra_cheese = input ("Do you want extra cheese ? Y or N")


if size == "S":
    bill += 15
    print ("Small Pizza is $15")
elif size == "M":
    bill += 20
    print ("Medium pizza is $20")
elif size  == "L":
    bill += 25
    print ("Large pizza is $25")
else :
    print ("you typed the wrong input")

if pepperoni =="Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


# Logical Operators
# A and B both conditions need to be true 
# C or D Only one condition needs to be true
# Not The condition must be false

