from seqtools import fastaToDict


fasta = fastaToDict("rosalind_sseq.txt")

fullString = list(fasta.values())[0]
subString = list(fasta.values())[1]

fullStringLength = len(fullString)
substringLength = len(subString)

# i = fullstring index
# j = substring index

j=0

for i in range(0, fullStringLength):
    if j > substringLength-1:
        break
    if fullString[i] == subString[j]:
        # print +1 to account for zero indexing
        print(i+1, end=" ") 
        i += 1
        j += 1
    else:
        i += 1
        j += 0






# Keeping this broken algo for posterity
# I tried nested for loops but that approach was not appropriate
# J would continue looping, rather than looking for one solution and stopping
# It was bad.
# Needed a ratchet, not a loop!

#for i in range(0, fullStringLength):
#    for j in range(0, substringLength):
#        if fullString[i] == subString[j]:
#            # print +1 to account for zero indexing
#            print("found it! i: ", i, " j: ", j)
#            #print(i+1, end=" ") 
#            i += 1
#            j += 1
#        else:
#            i += 1
#            j += 0
