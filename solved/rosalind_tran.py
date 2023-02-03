import seqtools


fasta = seqtools.fastaToDict("rosalind_tran.txt")

input1 = list(fasta.values())[0]
input2 = list(fasta.values())[1]

transitions = 0
transversions = 0


for x in range(0, len(input1)):
    if input1[x] == 'A':
        if input2[x] == 'C':
            transversions += 1 
        if input2[x] == 'T':
            transversions += 1 
        if input2[x] == 'G':
            transitions += 1
    if input1[x] == 'C':
        if input2[x] == 'A':
            transversions += 1 
        if input2[x] == 'T':
            transitions += 1
        if input2[x] == 'G':
            transversions += 1 
    if input1[x] == 'T':
        if input2[x] == 'A':
            transversions += 1
        if input2[x] == 'C':
            transitions += 1
        if input2[x] == 'G':
            transversions += 1
    if input1[x] == 'G':
        if input2[x] == 'A':
            transitions += 1
        if input2[x] == 'C':
            transversions += 1 
        if input2[x] == 'T':
            transversions += 1 
            
print(transitions / transversions)


