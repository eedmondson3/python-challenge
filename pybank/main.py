# Import Modules to Locate and Access CSV File
import os
import csv

# Access budget_data CSV
budget_data = os.path.join("resources", "budget_data.csv")

# Variables
month_count = 0
net_profit= 0
p_l_changes = []
# Discovered that dictionaries are more efficient than lists with large datasets @ https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/
max_increase = {"date": "", "amount": 0}
max_decrease = {"date": "", "amount": 0}

# Open and Read budget_data CSV
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skipping the Headers
    next(csv_reader)

    # Iteration for looping through rows
    for row in csv_reader:
        # Counting the Months
        month_count += 1

        # Net Profit Calculation:
        net_profit += int(row[1])

        # Calculate P&L Changes and looping through rows
        if month_count == 1:
            prev_profit = int(row[1])
        else:
            change = int(row[1]) - prev_profit
            p_l_changes.append(change)
            prev_profit = int(row[1])

            # Greatest increase & decrease in profit
            if change > max_increase["amount"]:
                max_increase["date"] = row[0]
                max_increase["amount"] = change
            elif change < max_decrease['amount']:
                max_decrease['date'] = row[0]
                max_decrease['amount'] = change

# Calculate P/L Average - Round fx found @ https://datagy.io/python-round-2-decimals/
p_l_avg = round(sum(p_l_changes) / len(p_l_changes), 2)

# Output Pathing
folder = "pybank"
analysis=os.path.join(folder , "analysis.txt") 

# Writing to analysis.txt
with open("analysis.txt", "w") as analysis:

    # Outputs for Analysis - /n Fx found at https://stackoverflow.com/questions/60885439/how-the-n-symbol-works-in-python
    analysis.write("Pybank Analysis\n")
    analysis.write("-----------------------------------------------\n")
    analysis.write(f"Total Number of Months: {month_count}\n")
    analysis.write(f"Net Total of Profit/Losses: ${net_profit}\n")
    analysis.write(f"Average P/L Change: ${p_l_avg}\n")
    analysis.write(f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['amount']})\n")
    analysis.write(f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['amount']})\n")