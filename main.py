print("==============================================")
print("VIT CANTEEN ORDER SYSTEM")
print("==============================================")
print("1.VIEW MENU")
print("2.PLACE ORDER")
print("3.VIEW CURRENT ORDER")
print("4.GENERATE BILL")
print("5.EXIT")
choice = int(input("enter your choice"))
if choice == 1:
    print("you selected view menu")
elif choice == 2:
    print("you selected place order")
elif choice == 3:
    print("you selected view current order")
elif choice == 4:
    print("you selected generate bill")
elif choice == 5:
    print("Thank you for choosing VIT Canteen")
else:
    print("invalid choice")