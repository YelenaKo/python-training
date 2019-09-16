# n = int(input("enter the number "))
# print( n >= 100 )

########################################


# a = input("Print Spathiphyllum " )
# if a == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif a == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not " + a + "!")


####################################################


income = float(input("Enter the annual income: "))
tax = 0

if income >= 85528:
    tax = (income - 85528) / 100 * 32 + 14839.02
elif income <= 0:
    tax = 0
else:
    tax = income / 100 * 18 - 556.02

tax = round(tax, 0)
print("The tax is:", tax, "thalers")