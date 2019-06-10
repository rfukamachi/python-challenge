#import libraries
import os, csv

#open csv file to read:
csv_path = os.path.join('Resources', 'election_data.csv')

#Lists to store the csv data:
VoterID = []
County = []
Candidate = []

#Initialize variables:
ttl_votes = 0
ttl_candidates = 0

#open the csv file and start reading in the data:
with open(csv_path, newline = "", encoding = "UTF8") as csv_file:
    
    #pull in rows of data as lists 
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #pull out header
    csv_header = next(csv_reader)

    for row in csv_reader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        

#total number of votes:
ttl_votes = len(VoterID)

#List of Unique Candidates:
UniqueCandidateSet = set(Candidate)
UniqueCandidates = list(UniqueCandidateSet)

#initialize candiate votes to zero:
CandidateVotes = []
for index in UniqueCandidates:
    CandidateVotes.append(0)

#start counting votes:
VoterRegistry = zip(VoterID, Candidate)

for EachVote in VoterRegistry:
    WhichCandidateIndex = UniqueCandidates.index(EachVote[1])
    CandidateVotes[WhichCandidateIndex] += 1

#calculate percentages of votes:
CandidatePercent = []
for index in CandidateVotes:
    VotePercentage = "{:.3f}%".format(float(index/ttl_votes*100))
    CandidatePercent.append(VotePercentage)


#zip it all up:
CandidatePolls = zip(UniqueCandidates, CandidatePercent, CandidateVotes)

#reverse sort so the winner is at the top of the list:

WinnerList = sorted(CandidatePolls)

for index in WinnerList:
    print(index)






# #output:
output = []
output.append("Election Results")
output.append("-" * 25)
output.append(f"Total Votes: {ttl_votes}")
output.append("-" * 25)

# output.append(f"Total: ${net_amt}")
# output.append(f"Average Change: ${avg_chg}")
# output.append(f"Greatest Increase in Profits: {grtst_incr_mo} (${grtst_incr_amt})")
# output.append(f"Greatest Decrease in Profits: {grtst_decr_mo} (${grtst_decr_amt})")


# #print to terminal:
# for i in output:
#     print(i)


# #create txt file to output:
# output_path = os.path.join('PyBankAnalysis.txt')
# with open(output_path, 'w') as txt_file: 
    
#     for i in output:
#         txt_file.write(i + '\n')


   
