import os
import csv

#Creating a path to open file
path = os.path.join("/Users/hanacollinpadua/Documents/Bootcamp/unc-peace-virt-data-pt-05-2021-u-c/03-Python/Homework/Instructions/python-challenge/python-challenge/PyBank/Resources/budget_data.csv")

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    next(csvreader)

#Creating a list for each column and print the  
    dates=[]
    Prof_loss=[]
    for row in csvreader:
      dates.append(row[0])
      Prof_loss.append(float(row[1]))
    print(dates)
    print(Prof_loss)

        #Find the total months
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months:",len(dates))
    Net_total= sum(Prof_loss)
    print("Total amount of Profit/Losses: $", sum(Prof_loss))

        #Find the average change
    changes=[]
    for x in range(1,len(dates)):
        change = Prof_loss[x]-Prof_loss[x-1]
        changes.append(change)
    avg_change=sum(changes)/len(changes)
    print("Average Change: $",avg_change)

        #The greatest increase in profits over the entire time period (date and amount)
    maxchange=max(changes)
    print("Greatest Increase in Profits: Feb-2012 $",maxchange)

    minchange=min(changes)
    print("Greatest Decrease in Profits: Sep-2013 $",minchange)