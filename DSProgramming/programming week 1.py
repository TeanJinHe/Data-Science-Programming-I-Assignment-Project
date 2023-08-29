# x=1
# y=2
# temp=x
# x=y
# y=temp
# print(x,y)

# a=3
# b=4
# a,b=b,a
# print(a,b)

# name = input("input: ")
# profession = input("input: ")
# print(name + " likes the name " + name + " but he doesn’t likes to be a " + profession)

# birth = int(input("birth year = "))
# age = 2022- birth
# print("age = ",age)

# birth = int(input("birth year = "))
# age = 2022- birth
# print("age = " + str(age) + "years old")

# bill = float(input("Electric bill: RM"))
# payment = bill* 0.9
# print("payment= RM",payment)

# bill = float(input("Electric bill: RM"))
# payment = bill* 0.9
# payment2dp = "{:.2f}". format(payment)
# print("payment= RM",payment2dp)

bill = float(input("Electric bill: RM"))
payment = bill* 0.9
print("payment= RM%.2f" %payment)