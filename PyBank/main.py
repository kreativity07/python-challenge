#Import dependencies for os.path.join
import os
import csv

#Declare the file path
budget_path = os.path.join("Resources", "budget_data.csv")

#Create specific lists for variables 
total_months = []
total_amount = []
average_change = []

#Read and store data of csv file
with open(budget_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total amount 
        total_months.append(row[0])
        total_amount.append(int(row[1]))

    # Iterate through the total amount in order to get the monthly amount
    for i in range(len(total_amount)-1):
        
        # Take the difference between two months and append to monthly average change
        average_change.append(total_amount[i+1]-total_amount[i])
        
# Obtain the max and min values of average change
max_increase_value = max(average_change)
max_decrease_value = min(average_change)

# Index the max and min of monthly average change 
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1 

# Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_txt_file = os.path.join("Resources", "Financial_Analysis.txt")

with open(output_txt_file,"w") as text_file:

    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {len(total_months)}", file=text_file)
    print(f"Total: ${sum(total_amount)}", file=text_file)
    print(f"Average Change: {round(sum(average_change)/len(average_change),2)}", file=text_file)
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})", file=text_file)
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})", file=text_file)

