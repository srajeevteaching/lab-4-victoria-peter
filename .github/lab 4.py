# Programmers: Peter and Victoria #
# Course: CS151, Dr. Rajeev
# Date: Thu Oct 7
# Lab: 4
# Program Inputs: Subscription Package, Data used
# Program Outputs: Money owed to mobile phone provider

package = (input("Input subscription package: "))
GB = int(input("Input GB used: "))
coupon = input("Do you have a coupon? (y/n) ")
price = 0
package = package.strip().lower()

if GB >= 0:
    if package == "green":
        price = 49.99 + (14.99 * (GB - 2))
        if price >= 75 and coupon == "y":
            price = price - 20
    elif package == "orange":
        price = 69.99 + (9.99 * (GB - 4))
    elif package == "purple":
        price = 99.99
    else:
        print("Invalid package.")
else:
    print("Invalid number of GB.")

print("Your price is: $" + str(price.__round__(3)))