#1
for i in range (10, 0, -1):
    print(i)
print("Liftoff!")

#2
c=0
d=0
for i in range (0, 5):
    a = int(input("Enter your age: "))
    if a<18:
        c= c + 1
    else:
        d= d + 1
print("Child tickets:", c)
print("Adult tickets:", d)


#3
# 1 3 5 7 9


#4
total = 0
for i in range (0 , 5):
    price = float(input("Enter the price of item: "))
    total = total + price
print("Total:", total)
print("Average:", total/5)


#5
while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Too short , try again.")   
    else:
        print("Password accepted.")
        break
     
     
     
#6
#output:
#70 
#40
#10
#-20
#Done


#7
steps = 1200
for i in range (1 ,8):
    print ("Day", i,":",i*steps)


#8
correctusername = "admin"
correctpassword = "1234"
k= 0
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correctusername and password == correctpassword:
        print("Welcome.")
        break
    else:
        print("Wrong username or password.")
        k= k + 1
        if k == 3:
            print("Account locked.")
            break
        
        
#Part B
#9
balance =500
amount= float(input("Enter amount to withdraw: "))
while amount != 0:
    if amount > balance:
        print("Insufficient funds.")
    elif amount < 0:
        print("Invalid amount.")
    else:
        balance = balance - amount
        print("Balance:", balance)
    amount = float(input("Enter amount to withdraw: "))
print("Goodbye")


#10
#Wrong PIN 2 attempts left
#Wrong PIN 1 attempts left
#Access granted
#Attempts used: 3


#11
p=0
total=0
max=-13
k=0
grade = float(input("Enter the grade : "))
while grade != -1:
    total = total + grade 
    k= k+1
    if grade >=51:
        p= p + 1
    if grade > max:
        max = grade
    grade = float(input("Enter the grade : "))
print("Passed:", p)
print("Failed:",k-p)
print("Highest:",max)
print("Average:",round(total/k))


#12
free_spaces = 20

while True:
    command = input("Command: ")
    
    if command == "stop":
        break
    elif command == "in":
        if free_spaces == 0:
            print("Garage full")
        else:
            free_spaces = free_spaces - 1
            print("Free spaces:", free_spaces)
    elif command == "out":
        if free_spaces == 20:
            print("Garage is empty")
        else:
            free_spaces = free_spaces + 1
            print("Free spaces:", free_spaces)
    else:
        print("Unknown command")











#13
maxtemp = -9999
k = 0
for i in range (1,8):
    temperature = int(input("Enter the degree of the day:"))
    print("Day",i,":", temperature)
    if temperature >30:
        k = k +1 
    if temperature > maxtemp:
        hottestday=i
        maxtemp= temperature
print("Hot days:",k)
print("Hottest day:", hottestday)


#14
password = "secret"
attempts = 0
while True :
    entered = input("Password: ")
    if entered == password :
        print("welcome")
        break
    attempts +=1
    if attempts == 3:
        print("Account locked")
        break
#Because attempts=0 is inside the loop, the counter always resets



#15





#16
money=50
d=50
k=1
while money < 1000:
    print ("Month",k,":",money)
    k=k+1
    d=d+10
    money = money + d
print("Month",k,":",money)
print("Goal reached in month",k)


#17
#105| Finds the smallest odd number that is divisible by 7 greater than 100
#The break stops the loop immediately when correct number is found



#Part C
#18
correct_pin = 2580
balance = 1000
attempts = 0
b = False

while attempts < 3:      
    pin = int(input("Enter the pin: "))
    if pin == correct_pin:
        print("Login successful!")
        b = True
        break
    else:
        attempts = attempts + 1
        if attempts == 3:
            print("Card blocked")
        else:
            print("Wrong PIN, try again.")

# Əgər giriş uğurlu olubsa, menyü dövrü başlayır
if b:
    while True:
        print("\n1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                print("Balance:", balance)
                
            case 2:
                deposit_amount = float(input("Enter amount to deposit: "))
                if deposit_amount <= 0:
                    print("Invalid amount")
                else:
                    balance = balance + deposit_amount
                    print("New balance:", balance)
                    
            case 3:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if withdraw_amount <= 0 or withdraw_amount > balance:
                    print("Invalid amount")
                else:
                    balance = balance - withdraw_amount
                    print("New balance:", balance)
                    
            case 4:
                print("Goodbye")
                break
                
            case _:
                print("Invalid choice")
                
                

#19
a = [0.05, 0.10, 0.20, 0.50, 1, 1.0]
coin = 0
while coin < 1.50:
    insert_coin = float(input("Insert coin: "))
    if a.count(insert_coin) == 0:
        print("Coin not accepted")
    else:
        coin = coin + insert_coin
        print("Total:", round(coin, 2))
print("Here is your water")
print("Change:", round(coin - 1.50, 2))



#20
s=0
for i in range (2,101):
    k=0
    for j in range(1,i):
        if i%j==0:
            k=k+1
           
    if k ==1:
        s=s+1
        print(i,end=" ")
print ("Total codes:", s)



#21
#101 102
#201 202
#301 302


#22
for floor in range(1, 6):
    if floor == 4:
        continue  
    print("Floor:", floor, end=" ")
    for room in range(1, 5):
        print(floor * 100 + room, end=" ")   
    print()  



#23
total_minutes = 480
served = 0

while total_minutes > 0:
    time_needed = int(input("Customer needs (min): "))
    
    if time_needed == 0:
        break
        
    if time_needed > total_minutes:
        print("Sorry, come back tomorrow")
        break
        
    total_minutes = total_minutes - time_needed
    served = served + 1

print("Customers served:", served)
print("Minutes left:", total_minutes)


#24
count_a = 0
count_b = 0
count_c = 0
spoiled = 0
while True:
    vote = input("Vote: ")  
    if vote == "end":
        break 
    if vote == "A":
        count_a = count_a + 1
    elif vote == "B":
        count_b = count_b + 1
    elif vote == "C":
        count_c = count_c + 1
    else:
        spoiled = spoiled + 1
print(f"A: {count_a} B: {count_b} C: {count_c}")
print("Spoiled:", spoiled)
if count_a == count_b or count_b == count_c or count_a == count_c:
    print("Winner: Tie")
elif count_a > count_b and count_a > count_c:
    print("Winner: A")
elif count_b > count_a and count_b > count_c:
    print("Winner: B")
else:
    print("Winner: C")
    
    
    
#