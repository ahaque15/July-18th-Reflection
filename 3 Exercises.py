
user_input = int(input("How many hours would you like to convert into minutes? "))

print(str(user_input) + " hours is equal to " + str(60 * user_input) + " minutes")



user_input_2 = (input("Would you like Option 1, to convert hours into minutes, or Option 2, to convert minutes into hours? Enter 1 for Option 1, and Enter 2 for Option 2: "))

if(user_input_2 == "Option 1" or user_input_2 == "option 1" or user_input_2 == "1"):

    user_input_3: int = int(input("How many hours would you like to convert into minutes? "))

    print(str(user_input_3) + " hours is equal to " + str(60 * user_input_3) + " minutes")


else:

    user_input_4: int = int(input("How many minutes would you like to convert into hours? "))

    print(str(user_input_4) + " minutes is equal to " + str(int(user_input_4/60)) + " hours and " + str(int((user_input_4/60 - int(user_input_4/60)) * 60)) + " minutes, or, in decimal form, " + str(user_input_4/60) + " hours" )




user_input_5 = input("What word would you like to check the length of? ")

print("The length of the word " + str(user_input_5) + "is " + str(len(user_input_5)))



