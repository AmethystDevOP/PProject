# Personal Finance Tracker
# Created by: Yu Rumeng (IIT Madras BS Student)
# Purpose: Tracking daily expenses and calculating savings rate

def calculate_finances():
    print("--- Welcome to Your Personal Budget Analyzer ---")
    
    try:
        monthly_income = float(input("Enter your total monthly income (INR): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    expenses = {}
    
    while True:
        category = input("Enter expense category (or type 'done' to finish): ").lower()
        if category == 'done':
            break
        try:
            amount = float(input(f"Enter amount for {category}: "))
            expenses[category] = expenses.get(category, 0) + amount
        except ValueError:
            print("Invalid amount. Skipping this entry.")

    total_expenses = sum(expenses.values())
    savings = monthly_income - total_expenses
    savings_rate = (savings / monthly_income) * 100 if monthly_income > 0 else 0

    print("\n--- Financial Summary ---")
    print(f"Total Income:   ₹{monthly_income:,.2f}")
    print(f"Total Expenses: ₹{total_expenses:,.2f}")
    print(f"Total Savings:  ₹{savings:,.2f}")
    print(f"Savings Rate:   {savings_rate:.2f}%")

    if savings_rate < 20:
        print("Advice: Your savings are a bit low. Time to cut back on the 'Misc' spending!")
    else:
        print("Advice: Great job! You are building a solid financial cushion.")

if __name__ == "__main__":
    calculate_finances()