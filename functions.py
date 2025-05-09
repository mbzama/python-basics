def cal_expense(exp):
    """Calculate the total expense from a list of expenses."""
    total = 0
    for i in exp:
        total += i
    return total

alist = [1, 2, 3, 4, 5]
blist = [6, 7, 8, 9, 10]
clist = [11, 12, 13, 14, 15]

total_exp = cal_expense(alist)
print("Total Expense: ", total_exp)

total_exp = cal_expense(blist)
print("Total Expense: ", total_exp)

total_exp = cal_expense(clist)
print("Total Expense: ", total_exp)

