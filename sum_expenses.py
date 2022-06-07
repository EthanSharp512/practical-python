total = 0
expenses = []
num_expenses = int(input("Enter your number of expenses:"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print(f'You spent ${total} on lunch this week')