<!--                                                                                           Michelle Werner (4/24/2022)-->
# Election Analysis
---

## Project Overview


A Colorado Board of Elections employee, Tom, has asked for help with an election audit of a recent local congressional election. 
(Pictured: Tom's Colorado Counties)

<!--![Tom Colorado](summary_assets/TomColorado.png)-->
<img src="https://github.com/miwermi/election-analysis/blob/main/summary_assets/TomColorado.png" width="400" height="232" align="right" alt ="graphic: Tom's Colorado Counties">


The tasks for this election audit of Tom's precinct are:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

### Resources
* Data Source: election_results.csv
* Software: Python 3.7.9, Visual Studio Code, 1.6.6

## Election-Audit Results
This audit generated the following information about the election results:

 Election Results:
  - There were 369,711 votes cast in the election

 Counties:
  - Jefferson voters made up 10.5% of the total precinct vote with 38,855 voters
  - Denver voters made up 82.8% of the total precinct vote with 306,055 voters
  - Arapahoe voters made up 6.7% of the total precinct vote with 24,801 voters

 Largest County Turnout:
  - Denver

 Candidate Results:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received: 3.1% of the vote and 11,606 votes.

 The winner of the election was:
  - Diana DeGette who received 272,892 votes and 73.8% of the total votes.

### Code Overview
I wrote python code to calculate and provide the above information from a dataset that Tom supplied. If verified by the precinct, the code I have written will hopefully be able to be used to tally the same data from similar datasets for all precincts in the state.

The data Tom provided was a .csv file that included the following information:
<br />

    | Ballot ID | County  | Candidate |
    | --------- | ------- | --------- |
    | Content   | Content | Content   |

My code iterates through the file looking for distinct candidates and distinct counties, then counts the votes for each. The full code is pictured and linked below, and key portions are described below the images:
<br /><br />
<img src="https://github.com/miwermi/election-analysis/blob/main/summary_assets/code1.png" width="220" height="298" alt ="graphic: code (1)"> &nbsp;&nbsp; 
<img src="https://github.com/miwermi/election-analysis/blob/main/summary_assets/code2.png" width="220" height="298" alt ="graphic: code (2)"> &nbsp;&nbsp; 
<img src="https://github.com/miwermi/election-analysis/blob/main/summary_assets/code3.png" width="220" height="298" alt ="graphic: code (3)"> &nbsp;&nbsp; 
<br />
Pictured: Python code (<a href="https://github.com/miwermi/election-analysis/blob/main/summary_assets/code1.png">1</a> | <a href="https://github.com/miwermi/election-analysis/blob/main/summary_assets/code2.png">2</a> | <a href="https://github.com/miwermi/election-analysis/blob/main/summary_assets/code3.png">3</a>)
<br /><br />
Key portions of the code include: connecting with the .csv file provided; using conditional if statements and storing distinct information on the candidates who were voted for and the counties where people voted; tracking and counting each ballot for each; calculating the total votes and percentage of votes; and last but not least, printing the totals to a new file for Tom.

To connect with our source file (and to designate a spot for the write file), I created the variable "file-to-load" and used the python 'os' library function "os.path.join":

    #Loads the file from path
    file_to_load = os.path.join("resources", "election_results.csv")
    #Saves the file to a path
    file_to_save = os.path.join("analysis", "election_results.txt")

Two arrays were used to store the candidate and county options, and two dictionaries were used to hold the candidate and county votes:

    #Collects candidate options and votes
    candidate_options = []
    candidate_votes = {}

    #Collects county options and votes
    county_options = []
    county_votes = {}
    
To track the votes as we count them, the 'with' statement was used (with the file open...) and then a couple of conditional 'if's to determine whether or not the candidate and county were new... 

    #If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:

        #Add the candidate name to the candidate list
        candidate_options.append(candidate_name)

        #Start tracking candidate's vote count
        candidate_votes[candidate_name] = 0

    #Add each vote to that candidate's count <<COUNTVOTE
    candidate_votes[candidate_name] += 1

    #If the county does not match any existing county...
    if county_name not in county_options:

        #Add the existing county to the list of counties.
        county_options.append(county_name)

        #Start tracking the county's vote count
        county_votes[county_name] = 0

    #Add a vote to that county's vote count <<COUNTVOTE
    county_votes[county_name] += 1
    
To calculate the percentages, I needed a couple of new variables to hold the count - and the candidate or county - together... and a line of code to designate those variables to be used as 'float' data so math functions could be peformed on the data. For both county and candidate totals, this was done in for-loops:

  for county_name in county_votes:

      #Retrieve the county vote count
      covotes = county_votes.get(county_name)

      #Calculate the percentage of votes for the county
      covote_percentage = float(covotes) / float(total_covotes) * 100
      county_results = (
          f"{county_name}: {covote_percentage:.1f}% ({covotes:,})\n")    

  for candidate_name in candidate_votes:

      #Retrieve the candidate vote count and percentage
      votes = candidate_votes.get(candidate_name)

      #Calculate the percentage of votes for the candidate
      vote_percentage = float(votes) / float(total_votes) * 100
      candidate_results = (
          f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          
At the end of each of the above 'for' loops (within the loop), the largest county and winning candidate were calculated:

      #Calculate largest county:
      if (covotes > largest_county_count) and (covote_percentage > largest_county_percentage):
          largest_county_count = covotes
          largest_county = county_name
          largest_county_percentage = covote_percentage

      #Determine the winner!
      if (votes > winning_count) and (vote_percentage > winning_percentage):
          winning_count = votes
          winning_candidate = candidate_name
          winning_percentage = vote_percentage
                      

## Election-Audit Summary

By writing Python code to run through this dataset to find and count votes for each candidate and county in the file, I was able to provide Tom with the following information for his precinct:

    -------------------------
    Total Votes: 369,711
    -------------------------
    County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
    -------------------------
    Largest County Turnout: Denver
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------


Pictured: VScode Terminal Window results from running Python code. (<a href="https://github.com/miwermi/election-analysis/blob/main/summary_assets/VStermina.png">PNG</a> | <a href="https://github.com/miwermi/election-analysis/blob/main/results/election-results.txt">TXT</a>)

The Python code displays the results above on-screen during program run, but also writes the data to a text file (linked above), which is more useful to Tom and his constituents. 

Once these initial audit results are confirmed successful, I know Tom and the Colorado Board of Elections are hoping to collect similar data files from all Colorado precincts and use this code to automate election tabulation for all of Colorado, very exciting!  

There are two ways to do this:
 - The first would be to store similar .csv files in a repository and use the python 'listdir' to find all of the files in the repository and to then create a new variable and array with a 'for' loop to pull every file in the repository through the program and then also make sure a similar index was added to the file name and loop through writing multiple results files.
<br />

    #Import list of files
    from os import listdir
    from os.path import isfile...
    
    #Store and loop through the (hopefully well-named) file list.  (All other already written code would be placed within this loop.)
    files_to_load = []
    for...

 - The second would be to add a column (or two) to the main data file and pull the data in for precinct as well (and/or state!), then duplicate the blocks for finding the totals, largest number, and calculating the percentage for those as well.

    | Ballot ID | Precinct | County  | Candidate |
    | --------- | -------- | ------- | --------- |
    | Content   | Content  | Content | Content   |

Ideally, the final code would also search for distinct Ballot IDs -- and ultimately Voter IDs, if it were possible to gather and use that information. Since elections are typically anonymous, there is a likely margin of error on the accuracy of the data collected (especially when independent units - districts, states, etc. - do not use the same standard voter IDs or the same standards for ballots). Voter IDs and Ballot IDs will most likely never be stored in the same data source as voting information - ever - due to the need to protect the privacy of the voter. However, I would feel much better about my code being used to handle additional datasets if broadly-standardized data could be collected -- and if I could run a few queries to find duplicates or quirky-looking anomalies in the new data and decide what might be best to do about them. 

Perfect data is always the dream!
