#import libraries
import os, csv

#open csv file to read:
csv_path = os.path.join('Resources', 'budget_data.csv')

#Lists to store the csv data:
dates = []
profit_loss = []
changes = []

#Initialize variables:
net_amt = 0
ttl_chg = 0

#open the csv file and start reading in the data:
with open(csv_path, newline = "", encoding = "UTF8") as csv_file:
    
    #pull in rows of data as lists 
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #pull out header
    csv_header = next(csv_reader)

    for row in csv_reader:
        dates.append(row[0])
        profit_loss.append(int(row[1]))
        net_amt += int(row[1])


#total number of months:
ttl_mo = len(dates)

#changes between months:
for index in range(ttl_mo):
    if index == 0:
        changes.append(0)
    else:
        changes.append(profit_loss[index] - profit_loss[index-1])


#calculate total changes:
for index in changes:
    ttl_chg += index

#find the greatest increase:        
grtst_incr_amt = max(changes)
grtst_incr_mo = dates[changes.index(max(changes))]

#find the greatest decrease:        
grtst_decr_amt = min(changes)
grtst_decr_mo = dates[changes.index(min(changes))]


#not working: 
avg_chg = "{:.2f}".format(float(ttl_chg/ttl_mo))

#output:
output = []
output.append("Financial Analysis ")
output.append("-" * 28)
output.append(f"Total Months: {ttl_mo}")
output.append(f"Total: ${net_amt}")
output.append(f"Average Change: ${avg_chg}")
output.append(f"Greatest Increase in Profits: {grtst_incr_mo} (${grtst_incr_amt})")
output.append(f"Greatest Decrease in Profits: {grtst_decr_mo} (${grtst_decr_amt})")


#print to terminal:
for i in output:
    print(i)


#create txt file to output:
output_path = os.path.join('PyBankAnalysis.txt')
with open(output_path, 'w') as txt_file: 
    
    for i in output:
        txt_file.write(i + '\n')


   
