

from pickletools import markobject


length = 5

inputString = '5 1 4 2 3'
input = inputString.replace(" ", "")

#print(input)

#data = list()
#for x in range(0, length):
#    data.append(input[x])




longestIncSeq = 0
incSubsequence = list()
longestDecSeq = 0
decSubsequence = list()


# start with 1, then 2, then 3 etc.
# i is the test number to FIND
# x is the test INDEX
for i in range(1, length):

    # these are for storing the test sequence
    # will replace longest seq at end of loop
    testIncSeqLength = 0
    testIncSubsequence = list()
    testDecSeqLength = 0
    testDecSubsequence = list()
    foundStart = False
    lastHit = 0

    for x in range(1, length):
        #scan for i, when found, note index
        #print("x: ", x, " i: ", i)
        if int(input[x]) == i and foundStart == False:
            testIncSeqLength += 1
            testIncSubsequence.append(input[x])
            lastHit = int(input[x])
            foundStart = True
            print("foundStart")
        if int(input[x]) > lastHit and foundStart == True:
            testIncSeqLength += 1
            testIncSubsequence.append(input[x])
            lastHit = int(input[x])

    print(testIncSubsequence)
    if len(testIncSubsequence) > len(incSubsequence):
        incSubsequence = testIncSubsequence

print(incSubsequence)
