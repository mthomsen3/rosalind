




fname = "rosalind_cons (2).txt"
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



# width = fasta.length + 1 (for rownames)
w = len(list(fasta.values())[0]) + 1
h = 4 #baseType
PWM = [[0 for y in range(w)] for x in range(h)]

PWM[0][0] = "A"
PWM[1][0] = "C"
PWM[2][0] = "G"
PWM[3][0] = "T"



# NOTE THAT PWM INDEX IS SHIFTED BY 1 TO ACCOMODATE LABELS AND THAT IS HARD CODED

for value in fasta.values():
    for base in range(0, len(value)):
        if value[base] == 'A':
            PWM[0][base+1] += 1;
        if value[base] == 'C':
            PWM[1][base+1] += 1;
        if value[base] == 'G':
            PWM[2][base+1] += 1;
        if value[base] == 'T':
            PWM[3][base+1] += 1;



consensusList = [0 for x in range(w)]

for x in range(1,w):
    consensusInt = 0;
    consensusBase = "";
    for y in range(0,h):
        if PWM[y][x] > consensusInt:
            consensusInt = PWM[y][x]
            consensusBase = PWM[y][0]
    consensusList[x] = consensusBase;

for x in range(1,len(consensusList)):
    print(consensusList[x], end = "")

print(" ")

for x in PWM:  # outer loop  
    for i in x:  # inner loop  
        print(i, end = " ") # print the elements  
    print()  



