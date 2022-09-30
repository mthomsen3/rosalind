from queue import Full
from urllib.request import urlopen
import tempfile
import re

fasta = {};
uniProtIDs = []
fullUniProtIDs = []


# N{P}[ST]{P}


fname = "rosalind_mprt.txt"

file = open(fname, "r")
for line in file.readlines():
    fullUniProtIDs.append(line.strip('\n'));
    uniProtIDs.append(line.strip('\n').split('_')[0]);

print(uniProtIDs)

#url = "http://www.uniprot.org/uniprot/" + uniProtIDs[0] + ".fasta"



def addRawFastaToDict(rawfasta):
    for line in rawfasta.splitlines():
        if not line:
            continue
        # create the sequence name in the dict and a variable
        if line.startswith('>'):
            active_sequence_name = line.strip('\n')
            if active_sequence_name not in fasta:
                fasta[active_sequence_name] = ''
            continue
        # add the sequence to the last sequence name variable
        fasta[active_sequence_name] += line.strip('\n')


def getRawFastaFromLink(url):
    response = urlopen(url)
    rawfasta = response.read().decode("utf-8", "ignore")
    return rawfasta;

for x in range(0,len(uniProtIDs)):
    url = "http://www.uniprot.org/uniprot/" + uniProtIDs[x] + ".fasta"
    print(url)
    addRawFastaToDict(getRawFastaFromLink(url))


#print(getRawFastaFromLink(url))
#print(fasta)

#for match in re.finditer('N[^P][ST][^P]', 'ADSADNASARASMFDNSKDNASAAAAAA'):
#    print(match.start())
#for match in re.finditer(r'(?=(N[^P][ST][^P]))', 'ADSADNASASARASMFDNSKDNASAAAAAA'):
#    print(match.start())


#print(fasta)

i = 0   
for value in fasta.values():
    matches = []
    results = re.finditer(r'(?=(N[^P][ST][^P]))', value)
    for match in results:
        matches.append(match.start()+1)
    if len(matches) > 0:
        print(fullUniProtIDs[i])
        for match in matches:
            print(match, end = " ")
        print('\n')
    i += 1
