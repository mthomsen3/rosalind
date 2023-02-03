



# DOM PROBABILITIES
hohoProb = 1
hoheProb = 1
homuProb = 1
heheProb = 0.75
hemuProb = 0.5
mumuProb = 0




# DOM PROBABILITIES FOR 2 OFFSPRING
hohoProb = 1 * 2
hoheProb = 1 * 2
homuProb = 1 * 2
heheProb = 0.75 * 2
hemuProb = 0.5 * 2
mumuProb = 0 * 2



hoho = 18578
hohe = 19970
homu = 18273
hehe = 19068
hemu = 16023
mumu = 16290

total = (hoho * hohoProb) + (hohe * hoheProb) + (homu * homuProb) + (hehe * heheProb) + (hemu * hemuProb) + (mumu * mumuProb)

print(total)



