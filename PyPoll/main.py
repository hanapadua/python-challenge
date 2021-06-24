import os 
import csv 

#Making a path to open file
pollpath = os.path.join("unc-peace-virt-data-pt-05-2021-u-c/03-Python/Homework/Instructions/python-challenge/python-challenge/PyPoll/Resources/election_data.csv")

#Creating Polling dictionary
polling = {}

#Set counter to 0
rnumber = 0

#open + read csv

with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    next(csvreader)

    header = next(csvreader)
# Find total # of votes cast
    for row in csvreader:
        rnumber +=1

        if row[2] in polling:
            polling[row[2]] +=1
        else:
            polling[row[2]] = 1

total_votes=rnumber
print('     ')
print('   ')
print('Election Results')
print('------------------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------------------')

for word in polling:
        print (f'{word}: {round((polling[word]/rnumber*100),2)}00% ({int(polling[word])})')


m=max(polling, key=polling.get)
print('------------------------------')
print(f'Winner:    {m}')
print('------------------------------')
