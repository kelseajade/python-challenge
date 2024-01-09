import os

import csv

file_path = 'budget_data.csv'

total_months = 0
total_profit_loss = 0
previous_profit = 0
changes_in_profit_loss = []
dates = []

with open(file_path, newline='') as budget_data:
    csvreader = csv.reader(budget_data)
    header = next(csvreader)  
    for row in csvreader:
      
        total_months += 1

     
        total_profit_loss += int(row[1])

   
        current_profit = int(row[1])
        if total_months > 1:
            change = current_profit - previous_profit
            changes_in_profit_loss.append(change)
            dates.append(row[0])
        previous_profit = current_profit


avgchange = sum(changes_in_profit_loss) / len(changes_in_profit_loss)

max_increase = max(changes_in_profit_loss)
max_decrease = min(changes_in_profit_loss)


max_increase_date = dates[changes_in_profit_loss.index(max_increase)]
max_decrease_date = dates[changes_in_profit_loss.index(max_decrease)]

print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${avgchange:.2f}")
print(f"Greatest Increase: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease: {max_decrease_date} (${max_decrease})")

output_file = "analysis.txt"
with open(output_file, "w") as file:
output_file = "analysis.txt"
with open(output_file, "w") as file:
  file.write("Financial Analysis\n")
  file.write(f"Total Months: {total_months}\n")
  file.write(f"Total: ${total_profit_loss}\n")
  file.write(f"Average Change: ${avgchange:.2f}\n")
  file.write(f"Greatest Increase: {max_increase_date} (${max_increase})\n")
  file.write(f"Greatest Decrease: {max_decrease_date} (${max_decrease})\n")
