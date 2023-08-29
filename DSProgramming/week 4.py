# i=0
# while i<4:
#     i+=1
#     if i==2:
#         continue
#     print(i)

# i=0
# a=0
# num=int(input('Enter your number: '))
# while num>i:
#     i=i+1
#     a=a+i
# print(a)

# num=[1,2,5,6,13,21,34,55,67,71,73,99]
# newlist=[]
# for x in num:
#     x=x+2
#     newlist.append(x)
# print(newlist)

# student_name = 'James'
# mark = {'James': 90, 'Jules': 55, 'Arthur': 77}
# for student in mark:
#     if student== student_name:
#         print(mark[student])
#         break
#     else:
#         print('no found')

# import math
# def f(x):
#     y =math.exp(x)
#     return y
#
# print('Using for loop:')
# for x in range (0,5,2): #0,2,4
#     print("{:.2f}".format(f(x)))
# print()
# print('using while loop:')
# x=0
# while (x<=4):
#     print("{:.2f}".format(f(x)))
#     x+=2

# import math
# def f(x):
#     y =math.exp(x)+x**2-0.25
#     return y
#
# print('Using for loop:')
# for x in range (0,5,2): #0,2,4
#     print("{:.2f}".format(f(x)))
# print()
# print('using while loop:')
# x=0
# while (x<=4):
#     print("{:.2f}".format(f(x)))
#     x+=2

# numbers =[12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i%5==0:
#         if 150<i and 500>=i:
#             continue
#         elif i>500:
#             break
#         print(i)

# num1= int(input('Enter First Number: '))
# num2= int(input('Enter Second Number: '))
# odd=0
# even=0
# for i in range(num1, num2+1):
#     if i%2==0 and (num1 <= i <= num2):
#         even= even+1
#     else:
#         odd= odd+1
#
# print(f'Total of even numbers from {num1} until {num2} : {even}')
# print(f'Total of odd numbers from {num1} until {num2} : {odd}')

# scrnum= int(input('Enter a secret number(1~10): '))
# for guesscount in range(3):
#     guess= int(input('Guess the number(1~10): '))
#     if guess==scrnum:
#         print('You are Correct!')
#         break
#     else:
#         if guesscount==2:
#             print(f'You’ve used up all of your chance. The secret number is {scrnum}.')
#         else:
#             print('Try Again!')

# scrnum= int(input('Enter a secret number(1~10): '))
# limit=3
# for guesscount in range(1,limit+1):
#     guess= int(input('Guess the number(1~10): '))
#     if guess==scrnum:
#         print('You are Correct!')
#         break
#     else:
#         if guesscount==limit:
#             print(f'You’ve used up all of your chance. The secret number is {scrnum}.')
#         else:
#             print('Try Again.')

# scrnum= int(input('Enter a secret number(1~10): '))
# limit=0
# while limit<3:
#     limit= limit+1
#     guess= int(input('Guess the number(1~10): '))
#     if guess==scrnum:
#         print('You are Correct!')
#         break
#     else:
#         print('Try Again.')
#         if(limit==3):
#             print(f'You’ve used up all of your chance. The secret number is {scrnum}.')

# i=0
# while i<3:
#     j=0
#     while j<3:
#         print(i,j)
#         j=j+1
#     i=i+1

num1= int(input('Enter First Number: '))
num2= int(input('Enter Second Number: '))
for i in range(num1, num2+1):#1-23
    if i>1:#2
        for j in range(2,i):#2-22
            if i%j==0:
                break
        else:
            print(i, end=" ")

# row=int(input("row= "))
# for i in range (row):
#     for j in range (i+1):
#         print(j+1, end=" " )
#     print()

# row=int(input("row= "))
# for i in range (row):
#     for j in range (i+1):
#         print(j+1, end=" " )
#     print()

# row=int(input("row= "))
# for i in range (row):
#     for j in range (i):
#         print(i, end=" " )
#     print()

# rows = int(input("Enter number of rows: "))
# k = 0
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#     k = 0
#     print()

# rows = int(input("Enter number of rows: "))
# k = 0
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#     while k != (2 * i - 1):
#         print(k, end=" ")
#         k += 1
#     k = 0
#     print()

# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(3):
#     for j in range(3):
#         A[i][j] *= 10
# print(A)

# number=5
# while number>0:
#     print(number)
#     number-=1

# for a in [1,2,3,4]:
#     if a>3:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('Finish')

# import math
# i=1
# while (i<=5):
#     x= float(input(f"Enter your x{i} value : "))
#     if (-math.pi<x and x<1):
#         def f(x):
#             y = math.cos(x**2)
#             return y
#     elif (1<= x and x<3):
#         def f(x):
#             y = 1/x
#             return y
#     elif (3<= x and x< 5):
#         def f(x):
#             y = math.exp(-0.1*x)+0.5
#             return y
#     elif (x>= 5):
#         def f(x):
#             y = math.sin(x)
#             return y
#     else:
#         def f(x):
#             y = 0
#             return y
#
#     print("The value of x is {:.4f}".format(f(x)))
#     i+=1

# import math
# def f(x):
#     y =math.exp(x)+x**2-0.25
#     return y
#
# print('Using for loop:')
# for x in range (0,5,2): #0,2,4
#     print("{:.2f}".format(f(x)))
# print()
# print('using while loop:')
# x=0
# while (x<=4):
#     print("{:.2f}".format(f(x)))
#     x+=2

# import math
# for i in range (1,4):
#     t=int(input(f'Enter t{i} value: '))
#     if 0<t<8:
#         v=235*(t-2)
#         print(f"v({t})={v}")
#     elif 8<=t<16:
#         v=724+4*t
#         print(f"v({t})={v}")
#     elif 16<=t<26:
#         v=50*t + 9*(t-15)**2
#         print(f"v({t})={v}")
#     elif t>26:
#         v=2120*math.exp(-0.05*(t-26))
#         print(f"v({t})={v}")
#     else:
#         print(f"v({t})=0")

# (x1,y1)=(4,2)
# (x2,y2)=(2,0)
# print((x1+x2,y1+y2))
#
# a=[3]
# aa=a*2
# print(aa)
# print(len(aa))
#
# b=['banana',2,1,7,'yellow',4, 'lemon']
# print(b[3:-3])

# def f(i):
#     switcher = {
#         1: x+y,
#         2: x-y,
#         3: x*y, }
#     return switcher.get(i)
# 
#
# x = 1
# while x < 4:
#     y = 1
#     while y < 4:
#         print(f'x,y: {x},{y}')
#         print(f"f(x,y): {f(x)}")
#         y += 2
#     x += 1
