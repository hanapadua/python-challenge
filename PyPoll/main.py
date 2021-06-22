import os 
import csv 

#Making a path to open file
pollpath = os.path.join("unc-peace-virt-data-pt-05-2021-u-c/03-Python/Homework/Instructions/python-challenge/python-challenge/PyPoll/Resources/election_data.csv")
with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    next(csvreader)

#Creating columns and rows from Voter ID, County, and Candidate
    id=[]
    county=[]
    candidate=[]
    for row in csvreader:
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


#Creating Polling dictionary
polling = {}
# Find total # of votes cast
    for row in csvreader:
        rnum +=1

        if row[2] in polling:
            polling[row[2]] +=1
    else:
        polling[row[2]] =1