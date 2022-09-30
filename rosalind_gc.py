
#https://stackoverflow.com/questions/9557713/add-multiple-sequences-from-a-fasta-file-to-a-list-in-python










fname = "rosalind_gc (3).txt"

#sequences = {}
gcContent = {}
fasta = {}

def get_key(val):
    for key, value in fasta.items():
        if val == value:
            return key
    return "key doesn't exist"

    
def get_gckey(val):
    for key, value in gcContent.items():
        if val == value:
            return key
    return "key doesn't exist"
 

#with open(fname, "r") as file:
#    for line in file:
#        if line.startswith(">"):
#            line = line.strip() # remove trailing newline characters
#            ident = line # store the ident value
#        sequences[ident] = line # assign ident to next line sequence
        
#for value in fasta.values():
    #print(value)


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
print(fasta)

        
for value in fasta.values():
    #print(len(value))
    gc = 0
    for base in range(0, len(value)):
        if value[base] == 'C':
            gc += 1;
        if value[base] == 'G':
            gc += 1;

    gcRatio = (gc / len(value)) * 100
    #print(gc)
    #print(gcRatio)
    gcContent[get_key(value)] = gcRatio;

print(gcContent)

print(get_gckey(max(gcContent.values())))
print(round(max(gcContent.values()),5))