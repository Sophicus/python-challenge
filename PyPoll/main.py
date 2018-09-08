
# coding: utf-8

# In[9]:


import csv

tf = open('output.txt','w')

print("Election Results")
print("----------------------------")
tf.write("Election Results" + '\n')
tf.write("---------------------------" + '\n')

with open("election_data.csv", 'r') as f:
    csv_f = csv.reader(f, delimiter=',')
    next(f)
    
    votes = {}
    
    for row in csv_f:
        if row[2] in votes.keys():
            votes[row[2]] += 1
        else: 
            votes[row[2]] = 1

total = sum(votes.values())
print(f"Total Votes: {total}")
print("----------------------------")
tf.write(f"Total Votes: {total}" + '\n')
tf.write("---------------------------" + '\n')

for each in votes.items():
    candidate = each[0]
    vote_count = each[1]
    percent = format((vote_count * 100 // total), ".3f")
    print(f"{candidate}: {percent}% ({vote_count})")
    tf.write(f"{candidate}: {percent}% ({vote_count})" + '\n')

print("----------------------------")
print(f"Winner: {max(votes, key=votes.get)}")
print("----------------------------")         
tf.write("---------------------------" + '\n')
tf.write(f"Winner: {max(votes, key=votes.get)}" + '\n')
tf.write("---------------------------" + '\n')

tf.close()

