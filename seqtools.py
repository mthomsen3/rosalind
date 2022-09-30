







def fastaToDict(filename):
    fasta = {}
    with open(filename, "r") as file:
        for line in file:
            if not line:
                continue
            if line.startswith('>'):
                sname = line.strip('\n').strip('>')
                if line.strip('\n').strip('>') not in fasta:
                    fasta[line.strip('\n').strip('>')] = ''
                continue
            fasta[sname] += line.strip('\n').strip('>')
    return fasta



def reverseString(x):
    x = x[::-1]
    return x

def reverseCompString(i):
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
