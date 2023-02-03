


input = 'CCUACUUCACCGGUGUGAAGCCCGGUUAGUGGCACGCCCGACAGAAGGGCUUAGGCCCAAGUUAACUUUAGGUGUCAC'

# get base count
au = input.count('A') + input.count('U');
cg = input.count('C') + input.count('G');


# get pairs
auP = int(au / 2)
cgP = int(cg / 2)

#print(auP)


def calcP(p):
    if p > 0:
        return p * calcP(p-1)
    else:
        return 1

#print(calcP(auP))
#print(calcP(cgP))

print(calcP(auP)*calcP(cgP))






