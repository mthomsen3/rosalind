


#input = 'TCAATGCATGCGGGTCTATATGCAT'


fname = "rosalind_revp.txt"
fasta = {}
with open(fname, "r") as file:
    for line in file:
        if not line:
            continue
        if line.startswith('>'):
            sname = line.strip('\n').strip('>')
            if line.strip('\n').strip('>') not in fasta:
                fasta[line.strip('\n').strip('>')] = ''
            continue
        fasta[sname] += line.strip('\n').strip('>')



def reverseString(x):
    x = x[::-1]
    return x

def revComp(i):
    complement = ""
    for element in range(0, len(i)):
        if i[element] == 'T':
            complement += 'A'
        if i[element] == 'A':
            complement += 'T'
        if i[element] == 'C':
            complement += 'G'
        if i[element] == 'G':
            complement += 'C'
    return(reverseString(complement))


inputString = list(fasta.values())[0]

palindromePositions = {}


for x in range(4, 13):
    for y in range(0, len(inputString)-x+1):
        inputSnippet = inputString[y:(y+x)]
        print(inputSnippet)
        revCompSnippet = revComp(inputSnippet)
        if inputSnippet == revCompSnippet:
            palindromePositions[y+1] = x;
        y+=1
    x+=1



for i in palindromePositions:
    print(i, palindromePositions[i])












