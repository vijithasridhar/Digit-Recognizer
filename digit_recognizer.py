from sklearn.neural_network import BernoulliRBM
from sklearn.linear_model import LogisticRegression
# from sklearn.cross_validation import train_test_split
# from sklearn import metrics
import csv
import numpy as np
import time

IMAGE_SIZE = 28     # height and width of the image
NUM_TRAINING = 42000
NUM_TEST = 28000

training_data = np.empty([NUM_TRAINING, IMAGE_SIZE**2], dtype=int)
training_labels = np.empty(NUM_TRAINING, dtype=int)
test_data = np.empty([NUM_TEST, IMAGE_SIZE**2], dtype=int)

def read_csv(fName, rowCount, labels=False, headers=True):
    csvfile = open(fName, 'r')
    reader = csv.reader(csvfile)
    if headers:
        next(reader, None)  # skip the headers    
    i = 1
    for row in reader:
        if i > rowCount:
            print "Done reading in " + fName[:-4] + " data"
        if i % 1000 == 0:
            print "Reached row {0} of ".format(i) + fName[:-4] + " data"
        if "train" in fName:
            if labels:
                training_labels[i-1] = row[0]
            training_data[i-1] = np.asarray(row[1:])
        else:
            test_data[i-1] = np.asarray(row)
        i += 1
    print "Closing file " + fName
    csvfile.close()


def logreg():
    print "Fitting training data to labels using LogisticRegression..."
    start = time.time()
    logreg = LogisticRegression()

    logreg.fit(training_data, training_labels)
    mid = time.time()
    print "Fitted training data in {0} minutes and {1} seconds; now predicting test labels" \
        .format(str((mid-start)/60), str((mid-start) % 60))

    test_labels = logreg.predict(test_data)
    end = time.time()
    print "Test labels predicted in {0} minutes".format(str((end-mid)/60))
    return test_labels

def write_submission(test_labels):
    with open('test_labels.csv', 'w') as f:
        f.write("ImageId,Label\n")
        for i in range(len(test_labels)):
            f.write(str(i+1) + "," + str(test_labels[i]) + '\n')
    print "Wrote files to output"


if __name__ == "__main__":
    #read in csv
    read_csv("train.csv", NUM_TRAINING, labels=True, headers=True)
    read_csv("test.csv", NUM_TEST, labels=False, headers=True)

    write_submission(logreg())

