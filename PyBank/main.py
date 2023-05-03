# Opening and reading the CSV file
import csv
import os

with open('budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skipping header row
    next(csvreader)

    # Initializing variables
    total_months = 0
    net_total = 0
    prev_profit = 0
    profit_changes = []
    max_increase = 0
    max_decrease = 0

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment total_months
        total_months += 1

        # Add Profit/Loss to net_total
        net_total += int(row[1])

        # Calculate change in Profit/Loss from previous row
        if total_months > 1:
            change = int(row[1]) - prev_profit
            profit_changes.append(change)

            # Check for new max increase or max decrease
            if change > max_increase:
                max_increase = change
                max_increase_date = row[0]
            elif change < max_decrease:
                max_decrease = change
                max_decrease_date = row[0]

        # Set previous Profit/Loss to current row's Profit/Loss
        prev_profit = int(row[1])

    # Calculate average change in Profit/Loss
    avg_change = sum(profit_changes) / len(profit_changes)

#PRINTING RESULTS ONLY
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

#Writing file within same folder
#with open('financial_analysis.txt','w') as outfile:
#   outfile.write("Financial Analysis\n")
#   outfile.write("--------------------------\n")
#   outfile.write(f"Total Months: {total_months}\n")
#   outfile.write(f"Total: ${net_total}\n")
#   outfile.write(f"Average Change: ${avg_change:.2f}\n")
#   outfile.write(f"Greatest Increase in Profits: {max_increase_date}(${max_increase})\n")
#   outfile.write(f"Greatest Decrease in Profits: {max_decrease_date}(${max_decrease})\n")

#Writing Text File to Analysis Folder
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${avg_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {max_increase_date}(${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {max_decrease_date}(${max_decrease})\n")    

print(f"Results written to {output_path}")

