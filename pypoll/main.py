import os

file_name = "election_data.csv"
output_file = "BudgetAnalysis.txt"
csvpath = os.path.join(os.getcwd(), "Resources", file_name)
outpath = os.path.join(os.path.curdir, output_file)

with open(csvpath, 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')
data_lines = [line.strip().split(',') for line in lines[1:]]

candidate_counts = {}
for line in data_lines:
    candidate = line[2]  
    if candidate in candidate_counts:
        candidate_counts[candidate] += 1
    else:
        candidate_counts[candidate] = 1

total_count = sum(candidate_counts.values())

percentage_data = {candidate: (count / total_count) * 100 for candidate, count in candidate_counts.items()}

winner = max(percentage_data, key=percentage_data.get)

output_data = []
output_data.append("Election Results \n")
output_data.append("---------------------------------------- \n")
output_data.append(f"Total Votes: {total_count:.0f}\n")
output_data.append("---------------------------------------- \n")

for candidate, count in candidate_counts.items():
    percentage = percentage_data[candidate]
    output_data.append("{:<25} {:<05.3f}% ({:})\n".format(candidate, percentage, count))

output_data.append("****************************** \n")
output_data.append(f"Winner: {winner}\n")
output_data.append("****************************** ")

with open(outpath, 'w') as output_file:
    output_file.writelines(output_data)

for row in output_data:
    print(row)