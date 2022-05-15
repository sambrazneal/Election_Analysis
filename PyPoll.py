# The data we need to retrieve
# 1. The total number of votes cast 
# 2. A complete list of canidates who recieved votes
# 3. The percentage of votes each canidate won 
# 4. The total number of votes each canidate won 
# 5. The winner of the election based on popular vote. 

import csv 
import os
from wsgiref import headers 


# Assign a variable for a file to load and the path. 
file_to_load = '/Users/samanthaneal/Documents/Election_Analysis/Resources/election_results .csv'

# Assign a varible to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file. 
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.

     # Read the file object with the reader function 
     file_reader = csv.reader(election_data)
     
     # Print each row in the CSV file. 
     headers = next(file_reader)
     print(headers)


# Using the with statement open file as text 
with open(file_to_save, "w") as txt_file:

# Write some data to file 
     txt_file.write("Arapahoe\nDenver\nJefferson")
