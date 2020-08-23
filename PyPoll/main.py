import os
import csv


poll_csv = os.path.join("Resources", "election_data.csv")


vote = 0
candidates = []
candidate = []
vote_count = []
vote_percent = []

with open(poll_csv) as csvfile:



    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

   
    for row in csvreader:
       
        vote = vote + 1
       
        candidates.append(row[2])
        
    for x in set(candidates):

        candidate.append(x)
       
        candidate_vote = candidates.count(x)
        vote_count.append(candidate_vote)
       
        percentvote = (candidate_vote/vote)*100

        vote_percent.append(percentvote)
        
    maxcount = max(vote_count)
    winner = candidate[vote_count.index(maxcount)]
    
 

output_file = os.path.join("Resources","Analysis.txt")

with open('Analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(vote)+ "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate))):
        text.write(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ") " + "\n" )
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")






