last=[]
balance=0
lt=0
i=0
t=0
while(i<1):
print("Welcome to piggy Bank")
print("Enter 1 to deposit")
print("Enter 2 to withdraw")
print("Enter 3 to show last 10 transactions")
print("Enter 4 to display balance")
print("Enter 5 to quit")
x=int(input())
def deposit(amount):
global balance
global lt
global t
balance=balance+amount
lt=amount
if t<10:

        last.append(lt)
    else:
      
        for k in range(9):
            last[k]=last[k+1]
        last[9]=lt
    t=t+1
def withdraw(amount):
    global balance
    global lt
    global t
    if balance>=amount:
        balance=balance-amount
        lt=-amount
        if t<10:
       
            last.append(lt)
        else:
            for k in range(9):
                last[k]=last[k+1]
            last[9]=lt
        t=t+1
    else:
        print("Insufficient balance")

def statement():
    print("Balance=",balance)
    print("lt=",lt)
    print("no of total transactions:",t)
    print("\n")

def last10():
    global t
    if t<10:
        print("no of total transactions:",t)
      
        print(("list of last %d transactions:")%(t),last)
        print("\n")
    else:
        print("no of total transactions:",t)
   
        print("list of last 10 transactions:",last)
        print("\n")

def checkBal():
    print("Your current balance is:",balance)
    print("\n")

if x==1:
    v1=int(input("please enter value to deposit"))
    while(i<1):
        if(v1<0):
            print("invalid input enter a positive value")
            v1=int(input("please enter value to deposit"))
            print("\n")
        else:
            break
    deposit(v1)
    statement()

elif x==2:
    v2=int(input("please enter value to withdraw"))
    while(i<1):
        if(v1<0):
            print("invalid input enter a positive value")
            v1=int(input("please enter value to deposit"))
            print("\n")
        else:
            break
    withdraw(v2)
    statement()

elif x==3:
    last10()

elif x==4:
    checkBal()

elif x==5:
    break

else:
    print("Invalid input")
