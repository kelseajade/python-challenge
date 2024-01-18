import os

import csv
#create file path
file_path = 'budget_data.csv'
#define variables 
total_months = 0
total_profit_loss = 0
previous_profit = 0
changes_in_profit_loss = []
dates = []
#import data from csv, skip header
with open(file_path, newline='') as budget_data:
    csvreader = csv.reader(budget_data)
    header = next(csvreader)  
    for row in csvreader:
#count months        
        total_months += 1
#define the profit    
        total_profit_loss += int(row[1])
#formula for changing profit from one row to the next  
        current_profit = int(row[1])
        if total_months > 1:
            change = current_profit - previous_profit
            changes_in_profit_loss.append(change)
            dates.append(row[0])
        previous_profit = current_profit
#need the average total profit
avgchange = sum(changes_in_profit_loss) / len(changes_in_profit_loss)
#find maximum and minimum changes
max_increase = max(changes_in_profit_loss)
max_decrease = min(changes_in_profit_loss)
#say the month and amount of greatest changes
max_increase_date = dates[changes_in_profit_loss.index(max_increase)]
max_decrease_date = dates[changes_in_profit_loss.index(max_decrease)]
#print analysis
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${avgchange:.2f}")
print(f"Greatest Increase: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease: {max_decrease_date} (${max_decrease})")
#create output file and write analysis
output_file = "analysis.txt"
with open(output_file, "w") as file:
    output_file = "analysis.txt"
file.write("Financial Analysis\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${total_profit_loss}\n")
file.write(f"Average Change: ${avgchange:.2f}\n")
file.write(f"Greatest Increase: {max_increase_date} (${max_increase})\n")
file.write(f"Greatest Decrease: {max_decrease_date} (${max_decrease})\n")
