# Wrote this because I didn't include headers/numbering in the original digit recognizer 
# and I didn't want to run logreg again. It shouldn't be necessary now, the digit recognizer
# outputs correctly

# My initial submission was test_output.csv, but  with digit_recognizer would be test_labels.csv

import csv

csvfile = open('test_labels.csv', 'r')
reader = csv.reader(csvfile)  
test_labels = []
for row in reader:
    test_labels.append(int(row[0]))

with open('test_output.csv', 'w') as f:
    f.write("ImageId,Label\n")
    for i in range(len(test_labels)):
        f.write(str(i+1) + "," + str(test_labels[i]) + '\n')
print "Wrote files to output"