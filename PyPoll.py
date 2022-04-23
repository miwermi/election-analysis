#PseudoCode/ProjDescript...

# Data to call/retrieve:
#1. The total number of votes "cast"
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each canddiate won
#5. The winner of the election based on popular vote

#Importing datetime class
import datetime as dt
from pickletools import float8

#Setting now()
now = dt.datetime.now()

#Print now-time/present moment... :) ***
# print("The time right now is ", now)

#Assign a variable and name the path to load the elections_results.csv file 
# file_to_load = "resources/election_results.csv"

    #Open the file -- new variable for the open and r-ead function
    # election_data = open(file_to_load, "r")
        #Perform analysis
    #Close the file -- Important!!!
    # election_data.close()

    #python can do all of the above with a with statement see below (after imports)***

import csv
import os

#Assign a variable for the file to load and the path - run py from main election-analysis folder.
file_to_load = os.path.join("resources", "election_results.csv")

#Open the election results and read the file
#with open(file_to_load) as election_data:

    #Read the file with the reader function.
    # file_reader = csv.reader(election_data, delimiter=',') < delimiter not needed ?
    #file_reader = csv.reader(election_data)

    # Read and print the header row.
    #headers = next(file_reader)
    #print(headers)

    #Print the first item in each row of the CSV file.
    # for row in file_reader:
    #     print(row[0])

#Assign a variabe to save the path...
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    #Write some data to the file.
    # txt_file.write("COUNTIES IN THE ELECTION:\n-------------------------\n")

    #Write three counties to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson\n")

#Initialize a total vote counter.
total_votes = 0

#Candidate options array (empty)
candidate_options = []

#Candidate votes dictionary (empty)
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            #Start tracking candidate vote count.
            candidate_votes[candidate_name] = 0

        #Count votes
        candidate_votes[candidate_name] += 1

#Print the candidate list.
#print(candidate_options)

#Print the candidate list***
# print(candidate_votes)

#Print the total votes.
# print(total_votes)

for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #Print ~ candidate name and percentage of votes! ***
    # print(f"{candidate_name}: received {round(vote_percentage, 1)}% of the vote.")
    
    #Determining winning vote count and candidate ******************************
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine if votes are greater than winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true set winning_count = votes - and -  winning_percent = vote_percentage;  
        winning_count = votes
        winning_percentage = vote_percentage
        #Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
