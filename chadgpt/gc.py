def gc_content(dna_string):
    gc_count = dna_string.count("G") + dna_string.count("C")
    return 100 * gc_count / len(dna_string)

dna_strings = {}
current_id = ""

for line in open("input.txt"):
    line = line.strip()
    if line.startswith(">"):
        current_id = line[1:]
        dna_strings[current_id] = ""
    else:
        dna_strings[current_id] += line

max_id = ""
max_gc = 0
for id, dna_string in dna_strings.items():
    gc = gc_content(dna_string)
    if gc > max_gc:
        max_id = id
        max_gc = gc

print(max_id)
print(max_gc)