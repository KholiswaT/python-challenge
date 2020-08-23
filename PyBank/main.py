import os
import csv

#Import csv file  via file path

budgetcsv = os.path.join("Resources" , "budget_data.csv")


#Define Variables

profit = []
monthly_netchange = []
date = [] 
month = 0
totals = 0
netchange = 0
previous_profit = 0



with open(budgetcsv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_head = next(budget_reader)

    
    for row in budget_reader:    
      
      month = month + 1 

      #Add to lists , row[0] represents the first column in the spreadsheet containing the dates
      # row[1] represents the second column containing the profits/losses
      date.append(row[0])
      profit.append(row[1])

      totals = totals + int(row[1])

      current_profit = int(row[1])
      netchange_month = current_profit - previous_profit

      monthly_netchange.append(netchange_month)

      netchange = netchange + netchange_month
      previous_profit = current_profit

      average = (netchange/month) 
      

      maxprofits = max(monthly_netchange)
      minprofits = min(monthly_netchange)

      maxdate = date[monthly_netchange.index(maxprofits)]
      mindate = date[monthly_netchange.index(minprofits)]

# Create new output file for final results

output_file = os.path.join("Resources","Analysis.txt")

with open('Analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("Financial Analysis "+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("Total Months: " + str(month) + "\n")
    text.write("Total Profits: " + "$" + str(totals) +"\n")
    text.write("Average Change: " + '$' + str(int(average)) + "\n")
    text.write("Greatest Increase in Profits: " + str(maxdate) + " ($" + str(maxprofits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(mindate) + " ($" + str(minprofits) + ")\n")
    text.write("----------------------------------------------------------\n")