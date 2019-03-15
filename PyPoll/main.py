# Import dependencies
import os 
import csv

# Assign file location with the pathlib library
csvpath = os.path.join('Resources', 'election_data.csv')

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(csvpath, 'r') as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print the summary of the analysis
khan_percent = (khan_votes/total_votes) * 100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {khan_percent:.3f}% {[khan_votes]}")
print(f"Correy: {correy_percent:.3f}% {[correy_votes]}")
print(f"Li: {li_percent:.3f}% {[li_votes]}")
print(f"O'Tooley: {otooley_percent:.3f}% {[otooley_votes]}")
print("----------------------------")
print(f"Winner: {[key]}")
print("----------------------------")

# create a path to a text file in Resources folder
output_txt_file = os.path.join("Resources", "Election_Results.txt")

# write the Financial Analysis summary into a text file 
with open(output_txt_file, "w") as text_file:

    print("Election Results", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Khan: {khan_percent:.3f}% {[khan_votes]}", file=text_file)
    print(f"Correy: {correy_percent:.3f}% {[correy_votes]}", file=text_file)
    print(f"Li: {li_percent:.3f}% {[li_votes]}", file=text_file)
    print(f"O'Tooley: {otooley_percent:.3f}% {[otooley_votes]}", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Winner: {[key]}", file=text_file)
    print("----------------------------", file=text_file)