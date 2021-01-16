# Import modules
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    
    #Add the total vote count
    for row in file_reader:
        total_votes +=1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name]=0
    
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Print the candidate list        
print(candidate_votes)
# Create a filename variable to a direct or indirect path to the file.
#with open(file_to_save,"w") as txt_file:

#Write some data to the file
    #txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")


# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. The winner of the election based on popular vote.