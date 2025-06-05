exp = [230, 240, 250, 260, 270, 280, 290, 300]

total = 0

for i in exp:
    print(i)
    total += i

print("Total: ", total)

print('------------------')

print('Range demo')

for i in range(len(exp)):
    print('Month: ', i+1, ' - Expense: ', exp[i])