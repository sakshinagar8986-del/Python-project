#Q1
correct_pin="1234"
balance=10000
i=0
while i<4:
    user_pin=input("Enter the ATM pin  :")
    if user_pin!=correct_pin:
        if i==2:
            print("Card Blocked")
            break

        i+=1
        print("Wrong pin,left attempt",3-i)
    else:
        print("Logged in successfully")
        break    
lst=[]
while (user_pin==correct_pin):
    print("Select options from 1 to 4")
    print(" 1.Balance\n 2.Deposit\n 3.Withdraw\n 4.Exit")
    user_choice=int(input("enter your choice from 1 to 4 :"))
    if(user_choice==1):
        print(f"Current Balance :{balance:.2f}")
    elif(user_choice==2):
        deposit_amt=int(input("Enter deposite amount:"))
        if(deposit_amt>0):
            balance+=deposit_amt
            print(f"deposit amount is {deposit_amt},your total balance is {balance}")
            lst.append(["deposit:",deposit_amt])
            print(lst)
    elif(user_choice==3):
        withdraw_amt=int(input("enter withdraw amount:"))
        if(withdraw_amt>balance):
            print("Insufficient balance")
        else:
            balance-=withdraw_amt
            print(f"withdrawal amount is{withdraw_amt}.your total balance is {balance}")
            lst.append(["Withdraw:",withdraw_amt])
    elif(user_choice==4):
        for i in lst:
            for j in i:
                print(j,end="")
            print()
        print(f"User your total balance is {balance}")        
        print("Thank you!")
        break
    else:
        print("Invalid choice")
    

#Q2

students={"Aman":[85,90,78],"Riya":[92,88,95],"Zoya":[70,65,80]}
lst=[]
lsti=[]
for i in students:
    lsti.append(i)
    n=i
    sum=0
    for j in students[i]:
        sum+=j
    avg=sum/3
    lst.append(avg)
    print(f"{i} {sum/3:.2f}" ,end=" ")
    if(avg>=85):
        print("A")
    elif(avg>=70):
        print("B")
    elif(avg>=50):
        print("C")
    else:
        print("F")
max=0
for k in lst:
    if(k>max):
        max=k
idx=lst.index(max)
print("Topper:",lsti[idx])

while True:
    print("###option###")
    print("select one option(1,4)")
    print(" 1.Add student\n 2.View all \n 3.Show topper \n 4.Exit")
    user_choice=int(input("Enter your choice:"))
    
    if(user_choice==1):
        name=input("Enter name of new student:")
        mark1=int(input("Enter mark1:"))
        mark2=int(input("Enter mark2:"))
        mark3=int(input("Enter mark3:"))
        if(name in lsti):
            print("Student already exist")
        elif not(0<mark1 & mark2 & mark3<=100):
            print("Invalid marks")
        else:
            students.update({name:[mark1,mark2,mark3]})
    elif(user_choice==2):
        print(students)
    elif(user_choice==3):
        lst=[]
        lsti=[] 
        for i in students:
            lsti.append(i)
            sum=0
            for j in students[i]:
                sum+=j
            avg=sum/3
            lst.append(avg)
        max=0
        for k in lst:
            if(k>max):
                max=k
        idx=lst.index(max)
        print("Topper:",lsti[idx])
  
        
    elif(user_choice==4):
        print("Goodbye!")
        break


    







