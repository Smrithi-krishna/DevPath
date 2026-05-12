# Personal Expense Tracker Starter Code

expenses = []

def add_expense(amount, category):
    expenses.append({
        "amount": amount,
        "category": category
    })

def view_expenses():
    for expense in expenses:
        print(expense)

if __name__ == "__main__":
    print("Expense Tracker Started")