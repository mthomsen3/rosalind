from imghdr import tests
import re

#fasta = {'>Rosalind_1':'GATTACA', '>Rosalind_2': 'TAGACCA', '>Rosalind_3': 'ATACA'}

fname = "rosalind_lcsm.txt"
fasta = {}

with open(fname, "r") as file:
    for line in file:
        if not line:
            continue
        # create the sequence name in the dict and a variable
        if line.startswith('>'):
            sname = line.strip('\n')
            if line.strip('\n') not in fasta:
                fasta[line.strip('\n')] = ''
            continue
        # add the sequence to the last sequence name variable
        fasta[sname] += line.strip('\n')
#print(fasta)

# scan through input string
# find first match, if it is less than string.length, then move endIndex
# if match not found, move startIndex and endIndex to scan for larger string


def isSubstringFound(subString, testString):
    # NOTE - will not identify overlapping matches, but shouldn't matter in 
    # this application since we are only searching for ONE possible match
    matches = []
    results = re.finditer(subString, testString)
    for match in results:
        matches.append(match.start()+1)
    if len(matches) > 0:
        return True
    else:
        return False
    

#isSubstringFound("NA","JKLKJDSNALKJDS")
#for value in fasta.values():
#    results = re.finditer(r'(?=(N[^P][ST][^P]))', value)



testFasta = list(fasta.values())[0]
#print(testFasta)

lcs = ""

startIndex = 0
endIndex = 1
while endIndex < len(testFasta):
    testString = testFasta[startIndex:endIndex]
    #print(testString)

    falseCount = 0
    for value in fasta.values():
        if isSubstringFound(testString, value) == False:
            falseCount += 1

    if falseCount > 0:
        # shift entire frame by 1
        startIndex += 1
        endIndex +=1
    else:
        # present in all values, so lengthen reading frame
        endIndex +=1
        lcs = testString

print(lcs)









