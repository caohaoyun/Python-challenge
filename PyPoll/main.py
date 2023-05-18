#Import os and csv
import os
import csv

#cwd = os.getcwd()  # Get the current working directory (cwd)
#print("Files in %r: %s" % (cwd, files))
#Open election_data.csv
election_data = os.path.join("Resources","election_data.csv")
with open(election_data,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #exclude the header row
    next(csvreader)
    ballot_count = 0
    #A complete list of candidates who received votes
    candidates_dic = {}
    for row in csvreader:    
        #The total number of votes cast 
        ballot_count += 1  
        #The total number of votes each candidate won  
        if (row[2] in candidates_dic):
            candidates_dic[row[2]] += 1 
        else:
            candidates_dic[row[2]] = 1
        
    print("Election results" )
    print("-----------------------------------------")    
    print("Total Votes: " + str(ballot_count)) 
    print("-----------------------------------------")     
    
    #The winner of the election based on popular vote
    winner = ""
    max_count = 0
    for x in candidates_dic:
        count = candidates_dic.get(x)
        if (count > max_count): 
            max_count = count
            winner = x
        #The percentage of votes each candidate won
        count_percentage = count/ballot_count
        print(x + ": " + str(round(count_percentage*100, 3)) + "% (" + str(count) + ")")  
    print("-----------------------------------------") 
    print("Winner: " + winner )
    print("-----------------------------------------")

#Print the results to new text file
analysis_results = os.path.join("Analysis","analysis_results")
with open("analysis_results.txt","w") as textfile:
    textfile.write("Election results\n"
"-----------------------------------------\n"
"Total Votes: 369711\n"
"-----------------------------------------\n"
"Charles Casper Stockham: 23.049% (85213)\n"
"Diana DeGette: 73.812% (272892)\n"
"Raymon Anthony Doane: 3.139% (11606)\n"
"-----------------------------------------\n"
"Winner: Diana DeGette\n"
"-----------------------------------------\n")

