print("======================================")
print("       VIT CANTEEN ORDER SYSTEM")
print("======================================")

# Canteen menu
menu = {
    1: ["Veg Sandwich", 50],
    2: ["Burger", 80],
    3: ["Pizza", 120],
    4: ["Pasta", 100],
    5: ["Cold Coffee", 60],
    6: ["Masala Maggi", 50]
}

# Dictionary to store the order
order = {}


# STEP 1: VIEW MENU
print("\n---------- CANTEEN MENU ----------")

for item in menu:
    print(item, ".", menu[item][0], "Rs.", menu[item][1])


# STEP 2: PLACE ORDER
print("\n---------- PLACE ORDER ----------")

while True:

    item = int(input("Enter item number (0 to finish): "))

    if item == 0:
        break

    if item in menu:

        quantity = int(input("Enter quantity: "))

        # Store item and quantity
        if item in order:
            order[item] = order[item] + quantity
        else:
            order[item] = quantity

        print(menu[item][0], "added to your order.")

    else:
        print("Invalid item number.")


# STEP 3: VIEW CURRENT ORDER
print("\n---------- CURRENT ORDER ----------")

total = 0

for item in order:

    name = menu[item][0]
    price = menu[item][1]
    quantity = order[item]

    amount = price * quantity

    print(name, "x", quantity, "=", "Rs.", amount)

    total = total + amount


# STEP 4: GENERATE BILL
print("\n---------- BILL ----------")

print("Total Bill = Rs.", total)


# STEP 5: EXIT
print("\nThank you for choosing VIT Canteen!")
print("======================================")