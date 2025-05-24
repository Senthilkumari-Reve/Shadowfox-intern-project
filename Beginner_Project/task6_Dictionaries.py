#1.Create a List of Tuples with Friends Names and Lengths
'''Make a list of at least 5 friends names

Create a list of tuples → each tuple should be:
(friend_name, length_of_name)'''

friends = ["Anjali", "Karthik", "Meera", "Vikram", "Divya"]

# Create list of tuples
name_lengths = [(name, len(name)) for name in friends]

print("Friends and their name lengths:", name_lengths)

#2.Compare Trip Expenses with a partner
'''Create two dictionaries:

    One for your expenses

    One for your partner’s expenses

Calculate total expenses for both

Find out:

    Who spent more

    Which category has the biggest difference'''

# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more.")
elif your_total < partner_total:
    print("Your partner spent more.")
else:
    print("You both spent the same.")

# Find category with biggest difference
max_diff = 0
diff_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_diff:
        max_diff = difference
        diff_category = category

print(f"The category with the biggest spending difference is '{diff_category}' with a difference of {max_diff}.")
