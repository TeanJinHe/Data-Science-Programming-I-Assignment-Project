# hot = False
# cold = False
# if hot:
#     print('It is a hot day. Drink plenty of water.')
# elif cold:
#     print('It is a cold day. Wear warm clothes.')
# else:
#     print('It is a lovely day.')
# print('Enjoy your day')
#
# weather= str(input('Weather: '))
# if weather== "hot":
#     print('It is a hot day. Drink plenty of water.')
# elif weather=="cold":
#     print('It is a cold day. Wear warm clothes.')
# else:
#     print('It is a lovely day.')
# print('Enjoy your day')
#
# loan = 50000
# has_good_credit= True
# has_high_income= False
#
# if has_good_credit and not has_high_income:
#     print('Eligible for loan with 10% downpayment')
#     downpayment = 0.1* loan
#     print(f' downpayment: RM%.2f'%downpayment)
# elif has_good_credit or has_high_income:
#     print('Eligible for loan with 20% downpayment')
#     downpayment = 0.2* loan
#     print(f' downpayment: RM{downpayment}')
#
# num= int(input('Enter number: '))
# if num >0:
#     print('positive')
# elif num <0:
#     print('negative')
# else:
#     print('Zero')
#
# num= int(input('Enter number: '))
# ans= num%2
# if ans == 0:
#     print('even')
# else:
#     print('odd')
#
# num= int(input('Enter number: '))
# if (num%2==0):
#     print('even')
# else:
#     print('odd')
#
# a= int(input('A= '))
# b= int(input('B= '))
# c= int(input('C= '))
# if a>b:
#     if a>c:
#         print('a is the biggest number')
# else:
#         print('c is the biggest number')
# else:
#     if b>c:
#          print('b is the biggest number')
#     else:
#          print('c is the biggest number')
#
# a= int(input('A= '))
# b= int(input('B= '))
# c= int(input('C= '))
# if a>b and a>c:
#         print('a is the biggest number')
# elif a<b and b>c:
#         print('b is the biggest number')
# else:
#         print('c is the biggest number')
#
# a= int(input('A= '))
# b= int(input('B= '))
# c= int(input('C= '))
# maximum=max(a,b,c)
# print(f'{maximum} is the biggest number')

# def day(i):
#     switcher = {
#         0: 'Sunday',
#         1: 'Monday',
#         2: 'Tuesday',
#         3: 'Wednesday',
#         4: 'Thursday',
#         5: 'Friday',
#         6: 'Saturday'
#     }
#     return switcher.get(i)
# print(day(3))
#
# i=int(input('Enter your place of birth code: '))
# def birth(i):
#     switch = {
#         1: 'Johor',
#         2: 'Kedah',
#         3: 'Kelantan',
#         4: 'Melaka',
#         5: 'Negeri Sembilan',
#         6: 'Pahang',
#         7: 'Pulau Pinang',
#         8: 'Perak',
#         9: 'Peelis',
#         10: 'Selangor',
#         11: 'Terengganu',
#         12: 'Sabah',
#         13: 'Sarawak',
#         14: 'WP Kuala Lumpur',
#         15: 'WP Labuan'
#     }
#     return switch.get(i)
# print(f'Your birth place is : {birth(i)}')

# weight= float(input('Enter weight: '))
# place = str(input('Shipping to Penisular or East: '))
# if (weight<1):
#     if (place=="Penisular"):
#         price= weight*6
#     else:
#         price= weight*7
# else:
#     if (place=="Penisular"):
#         price= weight*8
#     else:
#         price= weight*10
# respond = str(input('Want to buy insurans? Y/N : '))
# if (respond=="Y"):
#     price2dp=price+2
#     print(f'Your price is RM%.2f.'%price2dp)
# else:
#     print(f'Your price is RM%.2f.'%price)

# lab assignment 2
# if (1, 2):
# print('foo')//need to put space
#
# a=5
# if a in [1,2,3,4,5]
#  print('yes')// if need to put :
#
# a = 32
# b = 32
# if b > a:
#  print("b is greater than a")
# else:
#  print("a is greater than b")//add condition
#
#  num = float(input("Enter a
#  number: "))
#  if num >= 0:
#      if
#  num == 0:
#  print("Zero")
#  else:
#  print("Negative number")
#  else:
#  print("Positive number")//>= need to change <=

# if 18>=age<=59:
#     if

num = float(input("Enter a number: "))
if num <= 0:
    if num == 0:
        print("Zero")
    else:
        print("Negative number")
else:
    print("Positive number")
