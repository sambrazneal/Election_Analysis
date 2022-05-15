# The data we need to retrieve
# 1. The total number of votes cast 
# 2. A complete list of canidates who recieved votes
# 3. The percentage of votes each canidate won 
# 4. The total number of votes each canidate won 
# 5. The winner of the election based on popular vote. 

import csv 
import os

# Assign a variable for a file to load and the path. 
file_to_load = '/Users/samanthaneal/Documents/Election_Analysis/Resources/election_results .csv'

# Assign a varible to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter. 
total_votes = 0 

# Canidate options and canidate votes 
canidate_options = []

# Declare the empty dictionary 
canidate_votes = {}

# Winning Canidate and Winning Count Tracker 
winning_canidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file. 
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     
     # Read the header row 
     headers = next(file_reader)

     # Print each row in the CSV file. 
     for row in file_reader:
          # Add to total vote count
          total_votes += 1

          # Print the canidate name from each row
          canidate_name = row[2]

          # If the canidate does not match any existing canidate... 
          if canidate_name not in canidate_options:
               # Add it to the list of canidates
               canidate_options.append(canidate_name)

               # Begin tracking that canidate's vote count 
               canidate_votes[canidate_name] = 0 

          # Add a vote to that canidate's count 
          canidate_votes[canidate_name] += 1 

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

     # Print the final vote count to the terminal 
     election_results = (
          f"\nElection Results\n"
          f"--------------------------\n"
          f"Total Votes:{total_votes:,}\n"
          f"--------------------------\n")
     print(election_results, end="")

     # Save the final vote count to the text file 
     txt_file.write(election_results)

     # Determine the percentage of votes for each canidate by looping through the counts
     # Iterate through the canidate list 
     for canidate_name in canidate_votes:
          # Retrieve vote count of a canidate 
          votes = canidate_votes[canidate_name]
          #Calculate the percentage of votes 
          vote_percentage = float(votes) / float(total_votes) * 100 
          # Print out each canidate's name, vote count, and percentage of votes to the terminal 
          # print(f"{canidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          # Canidate Results to txt_file
          canidate_results = (f"{canidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          # Print each canidate, their vote count, and percentage
          print(canidate_results)

          # Save the canidate results to text file 
          txt_file.write(canidate_results)

     # Determine winning vote and canidate 
     # Determine if the votes are greater than the winning count 
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # if true then set winning_count = votes and winning percent = vote_percentage 
               winning_count = votes
               winning_percentage = vote_percentage
               # Set the winning_canidate equal to canidate's name
               winning_canidate = canidate_name

     winning_canidate_summary = (
          f"--------------------------\n"
          f"Winner: {winning_canidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"--------------------------\n")

     # print(winning_canidate_summary)