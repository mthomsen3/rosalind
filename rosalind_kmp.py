# Knuth-Morris-Platt algorithm
# Error table generation algorithm
# Based on pseudocode: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm


from seqtools import fastaToDict

fasta = fastaToDict("rosalind_kmp.txt")


W = []

for value in list(fasta.values()):
    for char in value:
        W.append(char)


length = len(list(fasta.values())[0]) 
T = [0] * (length + 1)


pos = 1     # position in output array (aka T)
cnd = 0     # next character of candidate substring

T[0] = 0

print(W)

#for x in range(pos, length):
while pos < length:
    if W[pos] == W[cnd]:
        T[pos] = T[cnd]
    else:
        T[pos] = cnd
        while cnd > 0 and W[pos] != W[cnd]:
            #print("looping")
            cnd = T[cnd]
    pos += 1
    cnd += 1
T[pos] = cnd

print(T)

### INCOMPLETE POOPY






# NOTES

# Proper prefixes of AYYYYY: AYYYY AYYY AYY AY A
# Proper suffixes of AYYYYY: YYYYY YYYY YYY YY Y