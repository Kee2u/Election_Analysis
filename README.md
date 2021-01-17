# Election_Analysis

## Project Overview
In this project, a Colorado Board of Elections employee tasked me with completing the election audit of a recent local congressional election. These were the requirements of the audit:
 1. Calculate the total number of votes cast
 2. Create a complete list of candidates who received votes.
 3. Calculate the total number of votes each candidate received.
 4. Calculate the percentage of votes each candidate won.
 5. Determine the winner of the election based on popular vote.
 6. Calculate the voter turnout for each county.
 7. Calculate the percentage of votes from each county.
 8. Determine the county with the highest turnout.

## Resources
   - Data Source: election_results.csv
   - Software: Python 3.7.6, Visual Studio Code, 1.52.1
   
## Summary
I used Python to extract and calculate the data I needed from election_results.csv. Then I sent the results to a text file. Here is the output:

<img src ="https://github.com/Kee2u/Election_Analysis/blob/main/resources/Results.PNG?raw=true" width = "350">
The analysis of the election shows that:
 - There were 369,711 votes cast in the election.
 
### Candidate Result:

   - The candidates were:
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
        
   - The candidate results were:
      - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
      - Diana DeGette received 73.8% of the votes and 272,892 votes
      - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes
        
   - The winner of the election was:
      -Diana DeGette who received 73.8% of the votes and 272,892 votes 
       
### County Results

   - The counties were:
      - Jefferson
      - Denver
      - Arapahoe
        
   - The county results were:
      - With 38,855 voters, Jefferson voters accounted for 10.5% of the total number of voters.
      - With 306,055 voters, Denver voters accounted for 82.8% of the total number of voters.
      - With 24,801 voters, Arapahoe voters accounted for 6.7% of the total number of voters.
        
   - The county with the highest turnout was:
      - Denver with 306,055 voters and 82.8% of the total number of voters

## Election-Audit Summary
This script can be used to calculate the winner and voter turnout by county for any election. Instead of counting votes by county, the election commission may be interested    
