# print("this is gayathri")
# print("welcome to kdkr")




# balance=10000
# def deposite(balance):
#     amount=float(input("enter your amount"))
#     balance+=amount
# def withdraw(balance):
#     amount=float(input("enter your amount"))
#     if amount<=balance:
#         balance-=amount
#         print("sucessfully completed")
#     else:
#         print("insufficient")



# balance = 10000

# def deposit(balance):
#     amount = float(input("Enter your amount: "))
#     balance += amount
#     print("Successfully deposited.")
#     return balance

# def withdraw(balance):
#     amount = float(input("Enter your amount: "))
#     if amount <= balance:
#         balance -= amount
#         print("Successfully completed.")
#     else:
#         print("Insufficient balance.")
#     return balance
# balance = deposit(balance)
# print("Balance:", balance)

# balance = withdraw(balance)
# print("Balance:", balance)
    





# balance = 10000

# def deposit(balance):
#     amount = float(input("Enter deposit amount: "))
#     balance += amount
#     print("Amount deposited successfully.")
#     return balance

# def withdraw(balance):
#     amount = float(input("Enter withdrawal amount: "))
#     if amount <= balance:
#         balance -= amount
#         print("Withdrawal successful.")
#     else:
#         print("Insufficient balance.")
#     return balance

# while True:
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         balance = deposit(balance)
#     elif choice == 2:
#         balance = withdraw(balance)
#     elif choice == 3:
#         print("Current Balance:", balance)
#     elif choice == 4:
#         print("Thank you!")
#         break
#     else:
#         print("Invalid choice.")




# def kdkr(a,b,c,d=523271):
#     print("owner name :", a)
#     print("addres :", b)
#     print("phone :", c)
#     print("pin number :", d)
# kdkr("pen","delhi",12345)



# keyword
# def kdkr(p,t,r):
#     si=(p*t*r)/100
#     return si

# result=kdkr(t=2,p=10000,r=4)
# print(result)


# position argument


# def kdkr(p,t,r):
#     si=(p*t*r)/100
#     return si,p,t,r
# result,x,y,z=kdkr(1000,2,4)
# print(result)
# print("my p valude id :",x)
# print("my t value is :",y)
# print("my r value id :",z)



# def kdkr(p,t,r=4):
#     si=(p*t*r)/100
#     return si
# result=kdkr(150,t=10)
# print(result)







# def kdkr(p,t,r=4):
#     si=(p*t*r)/100
#     return si
# pen=100
# pencil=1000
# result=kdkr(pen,pencil,9222)
# print(result)





# function with list


# def kdkr(a):
#     for i in a:
#         print(i)
# a=[50,60,70,63,"guava"]
# kdkr(a)





# function with dict


# def kdkr(a):
#     print("my name is :", a['name'])
#     print("my ph num is :",a['ph num'])
#     print("my address is :",a['address'])

# my_input ={"name":"gayathri",
#    "ph num":9985133289,
#      "address":"chirrikurapadu"}
# kdkr(my_input)





# def my_prg(a):
#     b=a**2
#     c=a**3
#     d=a**4
#     return[b,c,d]     
# x=my_prg(2)
# print(x[1])
# print(y)
# print(z)




# orbitary argument single star


# def my_prg(*a):
#     b=a[0]+a[2]
#     c=a[3]+a[1]
#     d=a[0]+a[-1]
#     return[b,c,d]
# x=my_prg(20,30,40,60)
# print(x[0])
# print(x[2])


# keyword orbitary argument double star

# def my_prg(**a):
#     b=a['w']+a['m']
#     c=a['w']+a['k']
#     d=a['fruit']+a['j']
#     return[b,c,d]
# x=my_prg(w=20,kdkr=100,fruit="banana",m=30,n=60,k=200,j='mango')
# print(x[0])
# print(x[2])
# print(x[1])








# res=lambda x,y:x+y
# print(res(10,20))







