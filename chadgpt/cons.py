import re

def read_fasta(file):
    fasta = {}
    name = None
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]
            fasta[name] = ""
        else:
            fasta[name] += line
    return fasta

def consensus_string(fasta):
    dna_strings = list(fasta.values())
    n = len(dna_strings[0])
    m = len(dna_strings)
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    for i in range(n):
        for j in range(m):
            profile[dna_strings[j][i]][i] += 1
    consensus = ""
    for i in range(n):
        max_count = 0
        max_nucleotide = None
        for nucleotide in 'ACGT':
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus += max_nucleotide
    return consensus, profile

with open("input.txt", "r") as file:
    fasta = read_fasta(file)
    consensus, profile = consensus_string(fasta)
    print(consensus)
    for nucleotide in 'ACGT':
        print("{}: {}".format(nucleotide, " ".join(map(str, profile[nucleotide]))))
