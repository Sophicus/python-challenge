
# coding: utf-8

# In[16]:


import csv

tf = open('output.txt','w')

print("Financial Analysis")
print("---------------------------")
tf.write("Financial Analysis" + '\n')
tf.write("---------------------------" + '\n')

with open("budget_data.csv", 'r') as f:
    csv_f = csv.reader(f, delimiter=',')
    next(f)
    
    months = []
    total = []
    
    for row in csv_f:
        months.append(row[0])
        total.append(int(row[1]))      
    
m_change = [total[i+1]-total[i] for i in range(len(total)-1)]
avg_change = format(sum(m_change)/len(m_change),".2f")

print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total)}")  
print(f"Average Change: ${avg_change}")
tf.write(f"Total Months: {len(months)}" + '\n')
tf.write(f"Total: ${sum(total)}" + '\n')
tf.write(f"Average Change: ${avg_change}" + '\n')

with open("budget_data.csv", 'r') as f:
    csv_f = csv.reader(f, delimiter=',')
    next(f)
    
    mydict = dict(csv_f)
    newdict = {}
    
    for key, value in mydict.items():
        newdict[key] = int(value)

    max_k, max_v = max(newdict.items(), key = lambda x: x[1])
    min_k, min_v = min(newdict.items(), key = lambda x: x[1])

print(f"Greatest Increase in Profits: {max_k} (${max_v})")
print(f"Greatest Decrease in Profits: {min_k} (${min_v})")
tf.write(f"Greatest Increase in Profits: {max_k} (${max_v})" + '\n')
tf.write(f"Greatest Decrease in Profits: {min_k} (${min_v})" + '\n')

tf.close()

