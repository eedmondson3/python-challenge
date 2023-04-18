# Import Modules to Locate and Access CSV File
import os
import csv

# Variables
total_votes = 0
candidates = {}
winning_votes = 0
winner = ""

# Access election_data CSV
election_data = os.path.join("resources", "election_data.csv")

# Open and Read election_data CSV
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skipping the Headers
    next(csv_reader)

    # Iteration for looping through rows
    for row in csv_reader:
        
        # Total number of votes
        total_votes += 1

        # Counting votes for candidates
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] +=1
        else:
            candidates[candidate] = 1

    # Vote Percentage and Count for each Candidate
    for candidate in candidates:
        vote_count = candidates[candidate]
        vote_percentage = round(vote_count/total_votes * 100, 3)

        # Calculating the Winner
        if vote_count > winning_votes:
            winning_votes = vote_count
            winner = candidate

    # Output Pathing
    folder = "pypoll"
    analysis=os.path.join(folder , "analysis.txt") 

    # Writing to analysis.txt
    with open("analysis.txt", "w") as analysis:

        # Outputs for Analysis
        analysis.write("              Election Resulsts                \n")
        analysis.write("-----------------------------------------------\n")
        analysis.write(f"Total Number of Votes: {total_votes}\n")
        analysis.write("-----------------------------------------------\n")
        analysis.write(f"Candidate Breakdown:\n")

         # Vote Percentage and Count for each Candidate
        for candidate in candidates:
            vote_count = candidates[candidate]
            vote_percentage = round(vote_count/total_votes * 100, 3)
            analysis.write(f"{candidate}: {vote_percentage}% ({vote_count})\n")
        
        analysis.write("-----------------------------------------------\n")
        analysis.write(f"Winning Candidate: {winner}\n")
        analysis.write("-----------------------------------------------")