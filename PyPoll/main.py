import os 
import csv 

#Making a path to open file
pollpath = os.path.join("unc-peace-virt-data-pt-05-2021-u-c/03-Python/Homework/Instructions/python-challenge/python-challenge/PyPoll/Resources/election_data.csv")
with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    next(csvreader)

#Creating columns and rows from Voter ID, County, and Candidate



#Creating Polling dictionary
polling = {}
# Find total # of votes cast
for row in csvreader:
        rnum +=1

        if row[2] in polling:
            polling[row[2]] +=1
else:
        polling[row[2]] = 1

total_votes=rnum
print('------------------------------------')
print(f'Total Votes: {total_votes')
print('------------------------------------')

for word in polling:
    print (f'{word}: {round((polling[word]/rnum*100),2)}00% ({int(polling[word])})')


m=max(polling, key=polling.get
print('------------------------------')
print(f'Winner:    {m}')
print('------------------------------')