def DNA_strand(dna):
    complements = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C'}
    return "".join(complements[w] for w in dna)