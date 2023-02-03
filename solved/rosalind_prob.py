
import math

s = 'CCAATCATTCATGGCTGGACAGCCCCTCCACCGACGCCTATGATGCAGGTAGTAGCGCTGTGACGATAGGCTAAAACTATACGTATAGTACTCTACAC'

a = [0.102, 0.172, 0.223, 0.293, 0.365, 0.388, 0.458, 0.548, 0.583, 0.666, 0.727, 0.769, 0.846, 0.936]




def calcProbability(gcContent, testString):
    aProb = (1-gcContent)/2
    tProb = (1-gcContent)/2
    gProb = gcContent/2
    cProb = gcContent/2
    probability = 1;

    for x in range(0, len(testString)):
        if testString[x] == 'A':
            probability *= aProb
        if testString[x] == 'C':
            probability *= cProb
        if testString[x] == 'G':
            probability *= gProb
        if testString[x] == 'T':
            probability *= tProb

    return probability

b = []
for x in a:
    b.append(round(math.log10(calcProbability(x, s)),3))

for y in b:
    print(y, end=" ")



#print(math.log10(calcProbability(0.129, s)))













