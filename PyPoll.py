#PseudoCode/ProjDescript...

# Data to call/retrieve:
#1. The total number of votes "cast"
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each canddiate won
#5. The winner of the election based on popular vote

#Importing datetime class
import datetime as dt

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

#Assign a variable for the file to load and the path - no path join necessary.
file_to_load = os.path.join("resources", "election_results.csv")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file with the reader function.
    # file_reader = csv.reader(election_data, delimiter=',') < delimiter not needed ?
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    #Print the first item in each row of the CSV file.
    # for row in file_reader:
    #     print(row[0])


file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    #Write some data to the file.
    # txt_file.write("COUNTIES IN THE ELECTION:\n-------------------------\n")

    #Write three counties to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson\n")
