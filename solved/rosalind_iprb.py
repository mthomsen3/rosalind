import math




k = 19
m = 27
n = 30

x = 3 # number of groups
s = k + m + n # total number of individuals

#combinations = math.factorial(s)/(math.factorial(2)*(math.factorial(s-2)))

def possibleCombos(n, r):
    return math.factorial(n)/(math.factorial(r)*(math.factorial(n-r)))

print("possibleCombos: ", possibleCombos(s, 2))
pc = possibleCombos(s, 2)

hohoCombos = possibleCombos(k,2)
heheCombos = possibleCombos(m,2)
mumuCombos = possibleCombos(n,2)
hoheCombos = possibleCombos(k+m,2) - hohoCombos - heheCombos
homuCombos = possibleCombos(k+n,2) - hohoCombos - mumuCombos
hemuCombos = possibleCombos(m+n,2) - heheCombos - mumuCombos

# DOM PROBABILITIES
hohoProb = 1
heheProb = 0.75
mumuProb = 0
hoheProb = 1
homuProb = 1
hemuProb = 0.5

totalCombos = hohoCombos + heheCombos + mumuCombos + hoheCombos + homuCombos + hemuCombos
print("totalCombos: ", totalCombos)

hohoRatio = (hohoCombos / pc) * hohoProb
heheRatio = (heheCombos / pc) * heheProb
mumuRatio = (mumuCombos / pc) * mumuProb
hoheRatio = (hoheCombos / pc) * hoheProb
homuRatio = (homuCombos / pc) * homuProb
hemuRatio = (hemuCombos / pc) * hemuProb

finalProbability = hohoRatio + heheRatio + mumuRatio + hoheRatio + homuRatio + hemuRatio
print(finalProbability)

