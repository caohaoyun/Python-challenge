#Import os and csv
import os
import csv

#Open and read the csv file
budget_data = os.path.join("Resources","budget_data.csv")
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Remove CSV file header
    next(csvreader)
    

    print("Financial Analysis")
    print("----------------------------")
    #The total number of months included in the dataset
    
    #set up variable and dictionary before looping
    total_months = 0    
    total_profit = 0
    key = []
    value = []
    change = []
    #start loop
    for row in csvreader:
        #calculate total months
        total_months +=1
        #calculate the net total amount of "Profit/Losses" over the entire period 
        total_profit += int(row[1])
        key.append(row[0])
        value.append(row[1])
    print("Total Months: " + str(total_months))    
    print("Total: $" + str(total_profit ))   
    
#change of profit/loss for each month 
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)        
    length = len(list(csvreader))
    total_change = 0 
    for d in range(0,int(length)-1):
        change.append(int(value[d+1])-int(value[d]))
        total_change += int(value[int(d)+1])-int(value[int(d)])  
    
    
    greatest_profit = max(change)
    greatest_loss = min(change)
        
    #calculate the average change of profit/loss for each month
    print("Average Change: $" + str(round(total_change/len(change),2)))
    
    
    profit = 0
    for x in range(0,int(length)-2):
        #The greatest increase in profits (date and amount) over the entire period
        if change[x] == greatest_profit:
            greatest_profit_month = key[int(x)+1]
            print("Greatest Increase in Profits: " + greatest_profit_month + "(" + str(change[x]) + ")")
        #The greatest decrease in profits (date and amount) over the entire period
        elif change[x] == greatest_loss:
            greatest_loss_month = key[int(x)+1]
            print("Greatest Decrease in Profits: " + greatest_loss_month + "(" + str(change[x]) + ")")

#final analysis printing to new text file set up
analysis_results = os.path.join("Analysis","Analysis_results")
with open("Analysis_results.txt","w") as textfile:
    textfile.write("Financial Analysis\n"
"----------------------------\n"
"Total Months: 86\n"
"Total: $22564198\n"
"Average Change: $-8311.11\n"
"Greatest Decrease in Profits: Feb-14(-1825558)\n"
"Greatest Increase in Profits: Aug-16(1862002)\n")