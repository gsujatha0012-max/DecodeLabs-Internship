
total = 0
n = int(input("How many expenses do you want to enter? "))
for i in range(n):
    expense = float(input("Enter expense amount: "))
    total = total + expense

print("Total Spent:", total)
