

codonDictionaryRNA = {
    "TTT":"F",
    "TTC":"F",
    "TTA":"L",
    "TTG":"L",
    "TCT":"S",
    "TCC":"S",
    "TCA":"S",
    "TCG":"S",
    "TAT":"Y",
    "TAC":"Y",
    "TAA":"Stop",
    "TAG":"Stop",
    "TGT":"C",
    "TGC":"C",
    "TGA":"Stop",
    "TGG":"W",
    "CTT":"L",
    "CTC":"L",
    "CTA":"L",
    "CTG":"L",
    "CCT":"P",
    "CCC":"P",
    "CCA":"P",
    "CCG":"P",
    "CAT":"H",
    "CAC":"H",
    "CAA":"Q",
    "CAG":"Q",
    "CGT":"R",
    "CGC":"R",
    "CGA":"R",
    "CGG":"R",
    "ATT":"I",
    "ATC":"I",
    "ATA":"I",
    "ATG":"M",
    "ACT":"T",
    "ACC":"T",
    "ACA":"T",
    "ACG":"T",
    "AAT":"N",
    "AAC":"N",
    "AAA":"K",
    "AAG":"K",
    "AGT":"S",
    "AGC":"S",
    "AGA":"R",
    "AGG":"R",
    "GTT":"V",
    "GTC":"V",
    "GTA":"V",
    "GTG":"V",
    "GCT":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "GAT":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "GGT":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G",
}


codonDictionaryDNA = {
    "TTT":"F",
    "TTC":"F",
    "TTA":"L",
    "TTG":"L",
    "TCT":"S",
    "TCC":"S",
    "TCA":"S",
    "TCG":"S",
    "TAT":"Y",
    "TAC":"Y",
    "TAA":"",
    "TAG":"",
    "TGT":"C",
    "TGC":"C",
    "TGA":"",
    "TGG":"W",
    "CTT":"L",
    "CTC":"L",
    "CTA":"L",
    "CTG":"L",
    "CCT":"P",
    "CCC":"P",
    "CCA":"P",
    "CCG":"P",
    "CAT":"H",
    "CAC":"H",
    "CAA":"Q",
    "CAG":"Q",
    "CGT":"R",
    "CGC":"R",
    "CGA":"R",
    "CGG":"R",
    "ATT":"I",
    "ATC":"I",
    "ATA":"I",
    "ATG":"M",
    "ACT":"T",
    "ACC":"T",
    "ACA":"T",
    "ACG":"T",
    "AAT":"N",
    "AAC":"N",
    "AAA":"K",
    "AAG":"K",
    "AGT":"S",
    "AGC":"S",
    "AGA":"R",
    "AGG":"R",
    "GTT":"V",
    "GTC":"V",
    "GTA":"V",
    "GTG":"V",
    "GCT":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "GAT":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "GGT":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G",
}

fname = "rosalind_orf.txt"
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


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

orfs = []

def findOrfs(inputSeq):
    startIndex = []
    endIndex = None
    for index, codon in enumerate(chunker(inputSeq, 3)):
        #print(codonDictionary[codon], end="")
        if codonDictionaryRNA[codon] == 'M':
            if endIndex == None:
                startIndex.append(index)
            else:
                continue
        if codonDictionaryRNA[codon] == 'Stop':
            if len(startIndex) == 0:
                continue
            else:
                endIndex = index
                for x in range(0, len(startIndex)):
                    orfs.append(inputSeq[startIndex[x]*3:endIndex*3])
                    print("start: ", startIndex, " end: ", endIndex)
                startIndex = []
                endIndex = None

def reverseString(x):
    x = x[::-1]
    return x

def revComp(input):
    complement = ""
    for element in range(0, len(input)):
        if input[element] == 'T':
            complement += 'A'
        if input[element] == 'A':
            complement += 'T'
        if input[element] == 'C':
            complement += 'G'
        if input[element] == 'G':
            complement += 'C'
    return(reverseString(complement))


rf = list(fasta.values())[0]

# LOL need to trim if the sequence isn't divisible by 3
if (len(rf) % 3) != 0:
    print("SHIT")
    rf = rf[0:(len(rf)-(len(rf) % 3))]

rf0String = rf[0:]
rf1String = rf[1:len(rf)-2]
rf2String = rf[2:len(rf)-1]


rf0_revcomp = (revComp(rf0String))
rf1_revcomp = (revComp(rf1String))
rf2_revcomp = (revComp(rf2String))



findOrfs(rf0String)
findOrfs(rf1String)
findOrfs(rf2String)
findOrfs(rf0_revcomp)
findOrfs(rf1_revcomp)
findOrfs(rf2_revcomp)
#print(orfs)


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

uniqueOrfs = (unique(orfs))

for orf in uniqueOrfs:
    for codon in chunker(orf, 3):
        print(codonDictionaryDNA[codon], end="")
    print(" ")

            




