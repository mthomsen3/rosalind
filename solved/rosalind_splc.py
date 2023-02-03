


codonDictionary = {
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
fname = "rosalind_splc.txt"
fasta = {}

with open(fname, "r") as file:
    for line in file:
        if not line:
            continue
        # create the sequence name in the dict and a variable
        if line.startswith('>'):
            sname = line.strip('\n').strip('>')
            if line.strip('\n').strip('>') not in fasta:
                fasta[line.strip('\n').strip('>')] = ''
            continue
        # add the sequence to the last sequence name variable
        fasta[sname] += line.strip('\n').strip('>')
#print(fasta)

cds = list(fasta.values())[0]
print(cds)


# for each intron, search and delete from cds
# then translate remaining

for x in range(1, len(list(fasta.values()))):
    intron = list(fasta.values())[x]
    print(intron)
    cds = cds.replace(intron, '')

print(cds)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

for codon in chunker(cds, 3):
    print(codonDictionary[codon], end="")
