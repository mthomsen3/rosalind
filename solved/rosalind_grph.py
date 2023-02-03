




fname = "rosalind_grph.txt"
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


def get_key(val):
    for key, value in fasta.items():
        if val == value:
            return key
    return "key doesn't exist"


k = 3

graph = {}

for value in fasta.values():
    suffix = value[-3:]
    for comp in fasta.values():
        prefix = comp[:3]
        if  value == comp:
            continue
        else:
            if suffix == prefix:
                if get_key(value) not in graph.keys():
                    graph[get_key(value)] = [get_key(comp)]
                else:
                    print("add")
                    graph[get_key(value)].append(get_key(comp))

            
for key in graph:
    for value in graph[key]:
        print(key, value)
