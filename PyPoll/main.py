import csv

file_path = "election_data.csv"

#define variables
totalvotes = 0
candidatevotes = {}
candidates = []

# Read CSV
with open(file_path) as electiondata:
    csvreader = csv.reader(electiondata)
    
    # Skip header
    header = next(csvreader)
    
    # Loop through each row
    for row in csvreader:
      #votes
        totalvotes += 1
        
        #names
        candidate = row[2]
        
        # Update dictionary
        if candidate in candidatevotes:
            candidatevotes[candidate] += 1
        else:
            candidatevotes[candidate] = 1
            candidates.append(candidate)

# Calculate the percentage
percentage = {candidate: (votes / totalvotes) * 100 for candidate, votes in candidatevotes.items()}

# Find the winner of popular vote
winner = max(candidatevotes, key=candidatevotes.get)

# Print 
print("Election Results")
print(f"Total Votes: {totalvotes}")
for candidate in candidates:
    print(f"{candidate}: {percentage[candidate]:.3f}% ({candidatevotes[candidate]})")
print(f"Winner: {winner}")


# text file
with open("electionanalysis.txt", "w") as pollanalysis:
    pollanalysis.write("Election Results\n")
    pollanalysis.write(f"Total Votes: {totalvotes}\n")
    for candidate in candidates:
        pollanalysis.write(f"{candidate}: {percentage[candidate]:.3f}% ({candidatevotes[candidate]})\n")
    pollanalysis.write(f"Winner: {winner}\n")
 
