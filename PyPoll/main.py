# Opening and reading the CSV file
import csv
import os

with open('election_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment total_votes
        total_votes += 1
        
        # Add or update candidate's vote count
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    # Calculate the percentage of votes each candidate won
    candidate_percentages = {}
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = percentage

    # Find the winner of the election based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

# PRINTING RESULTS ONLY
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#Writing text file to Analysis Folder
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]
        textfile.write(f"{candidate}: {percentage: .3f}% ({votes})\n")
        textfile.write("---------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("---------------------\n")

print(f"Results written to {output_path}")







#Writing Results to text file
#with open('election_results.txt', 'w') as outfile:
#    outfile.write("Election Results\n")
#    outfile.write("------------------------\n")
#    outfile.write(f"Total Votes: {total_votes}\n")
#    outfile.write("------------------------\n")
#    for candidate, votes in candidate_votes.items():
#        percentage = candidate_percentages[candidate]
#        outfile.write(f"{candidate}: {percentage: .3f}% ({votes})\n")
#        outfile.write("---------------------\n")
#        outfile.write(f"Winner: {winner}\n")
#        outfile.write("---------------------\n")


#PRINTING and WRITING DIFFERETLY 
#with open('election_results.txt', 'w') as outfile:
#    print("Election Results")
#    print("-------------------------")
#    print(f"Total Votes: {total_votes}")
#    print("-------------------------")
#for candidate, votes in candidate_votes.items():
#    percentage = candidate_percentages[candidate]
#    print(f"{candidate}: {percentage: .3f}% ({votes})")
#    outfile.write(f"{candidate}: {percentage: .3f}% ({votes})\n")
#print("-------------------------")
#print(f"Winner: {winner}")
#print("--------------------------")
#outfile.write(f"Winner: {winner}\n")
#outfile.write("--------------------------\n")