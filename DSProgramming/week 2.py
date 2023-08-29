# bill=float(input('Electricity bill amount: RM'))
# total_payment=bill-(0.1*bill)
# total_payment_2DP="{:.2f}".format(total_payment)
# print('Your final payment is: RM'+total_payment_2DP)

# name='What a lovely day'
# print(len(name))
# print(name.count('a'))
# print(name.replace('o','i'))
# print(name.replace('lovely','great'))
# print(name[8:11])

# course = "Programming & Simulation"
# x=course[7:17]
# print(x)

# Mylist = [4, 5, 67, 'apple', 100, 'C', 3, 'duck']
# print (len(Mylist))

# Mytuple = (1, 3, 4, 5, 6, 4, 3, 5, 4, 5, 6, 4, 2, 4, 4)
# m=Mytuple.count(4)
# print(m)

# print('Welcome to Subway Laguna. Below are the admission price:')
# print('Adult (13 years old and above): RM75')
# print('Child (3-12 years old): RM45')
# print('Senior Citizen (55 years old and above): RM30')
# print('OKU: Free Admission')
# print('\nPlease insert the following details to proceed\n')
# name=str(input('Name: '))
# age=int(input('Age: '))
# print('\nPlease specify the quantity of tickets.')
# adult=int(input('ADULT (13 years old and above): '))
# child=int(input('CHILD (3-12 years old): '))
# senior=int(input('SENIOR (55 years old and above): '))
# oku=int(input('OKU: '))
# totalprice=((adult*75)+(child*45)+(senior*30)+(oku*0))
# totalwristbands=(adult+child+senior+oku)
# print(f"\nTotal Price: RM{totalprice}")
# print(f"Total wristbands printed are {totalwristbands}. Please collect your wristbands at the nearest counter.")
# print('\n****************************************************')
# print('Please note that you are required to provide your MyKad/OKU card for verification purpose.')
# print('Thank you.')
# print('****************************************************')

fruits=["kiwi", "melon", "lychee", "mango", "banana", "apple", "peach"]
fruits[2:5]=1,2,3
print(fruits[2:5])