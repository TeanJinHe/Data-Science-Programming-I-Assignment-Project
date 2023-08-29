# name = input('Enter Your Name: ')
# age = int(input('Enter Your Age: '))
#
# if age<18 or age>=60:
#     print("You're not eligible for the financial assistance")
# else:
#     category = int(input('Enter Your Category(singles=1,households/single_parent=2): '))
#     singles = 1
#     households = 2
#     if category==singles:
#         status = str(input('Enter Your Status(working=W/w,no_working=N/n): '))
#         working = 'w' or 'W'
#         no_working = 'n' or 'N'
#         if status==working:
#             income = float(input('Enter Your Income: RM'))
#             if income < 2500:
#                 cash = 250
#                 print(f"You're eligible for the financial assistance of amount RM%.2f"%cash)
#             else:
#                 print("You're not eligible for the financial assistance")
#         if status==no_working:
#             cash = 350
#             print(f"You're eligible for the financial assistance of amount RM%.2f"%cash)
#     elif category==households:
#         status = str(input('Enter Your Status(working=W/w,no_working=N/n): '))
#         working = 'w' or 'W'
#         no_working = 'n' or 'N'
#         if status==working:
#             income = float(input('Enter Your Income: RM'))
#             if income < 2500:
#                 child = int(input("Enter Number Of Child: "))
#                 if child==0:
#                     cash = 1000
#                 elif child<3:
#                     cash = 1300
#                 else:
#                     cash = 1700
#                 print(f"You're eligible for the financial assistance of amount RM%.2f"%cash)
#             elif income <= 4000:
#                 child = int(input("Enter Number Of Child: "))
#                 if child == 0:
#                     cash = 700
#                 elif child < 3:
#                     cash = 1000
#                 else:
#                     cash = 1200
#                 print(f"You're eligible for the financial assistance of amount RM%.2f"%cash)
#             elif income <= 5500:
#                 child = int(input("Enter Number Of Child: "))
#                 if child == 0:
#                     cash = 400
#                 elif child < 3:
#                     cash = 600
#                 else:
#                     cash = 800
#                 print(f"You're eligible for the financial assistance of amount RM%.2f"%cash)
#             else:
#                 print("You're not eligible for the financial assistance")
#         if status==no_working:
#             child = int(input("Enter Number Of Child: "))
#             if child == 0:
#                 cash = 1200
#             elif child < 3:
#                 cash = 1500
#             else:
#                 cash = 2000
#             print(f"You're eligible for the financial assistance of amount RM%.2f"%cash)
#     else:
#         print('valid error')

name=input('Please enter your name:')
age= int(input('Please enter your age:'))


if age<18 or age>59:
    print('You are not eligible for financial assistance')
else:
    household_category= str(input('Please enter your household category(S/s-single,M/m-married):'))
    if household_category=='S' or household_category=='s':
        working_status= str(input('Please enter your working status(W/w-working,N/n-Not working):'))
        if working_status=='W' or working_status=='w':
            household_income=int(input('Please enter your income:'))
            if household_income<=2500:
                cash=250
                print(f"You are eligible for the financial assistance of amount RM {cash}")
            else:
                print('You are not eligible for financial assistance')
        if working_status=='N' or working_status=='n':
            cash=350
            print(f"You are eligible for the financial assistance of amount RM {cash}")

    elif household_category=='M' or household_category=='m':
        working_status = str(input('Please enter your working status:'))
        if working_status == 'W' or working_status == 'w':
            household_income = int(input('Please enter your income:'))
            if household_income < 2500:
                noofchild=input('PLease enter number of children in your household:')
                if noofchild==0:
                    cash=1000
                elif noofchild==1:
                    cash=1300
                else:
                    cash=1700
                    print(f"You are eligible for the financial assistance of amount RM {cash}")

            elif household_income >=2500 and household_income<=4000:
                noofchild = input('PLease enter number of children in your household:')
                if noofchild == 0:
                    cash = 700
                elif noofchild == 1:
                    cash = 1000
                else:
                    cash = 1200
                    print(f"You are eligible for the financial assistance of amount RM {cash}")

            elif household_income >=4001 and household_income<=5500:
                noofchild = input('PLease enter number of children in your household:')
                if noofchild == 0:
                    cash = 400
                elif noofchild == 1:
                    cash = 600
                else:
                    cash = 800
                    print(f"You are eligible for the financial assistance of amount RM {cash}")
            else:
                print('You are not eligible for financial assistance')

        elif working_status=='N' or working_status=='n':
            noofchild = input('PLease enter number of children in your household:')
            if noofchild == 0:
                cash = 1200
            elif noofchild == 1:
                cash = 1500
            else:
                cash = 2000
                print(f"You are eligible for the financial assistance of amount RM {cash}")