#!/Users/ATEMIA/miniconda3/bin/python

### Exercise 1
# Calculate the % GC and % AT content in the trna sequence

#Question 1
trna = 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

A_count = trna.count('A')
C_count = trna.count('C')
G_count = trna.count('G')
T_count = trna.count('T')
total_count = (A_count + C_count + G_count + C_count)
perc_GC = ((G_count + C_count) / (total_count)) * 100
print("The GC content in the trna is %.2f" % perc_GC, "percent")
perc_AT = 100 - perc_GC
print("The AT content in the trna is %.2f" % perc_AT, "percent")

### Exercise 2
# The find the first, last and the 5th amino acids in the sequence. 
# Restriction enzyme "TCCGGA". The first restriction site in the sequence: AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA

# Question 1
aa = "MNKMDLVADVAEKTDLSKAKATEVIDAVFA"
aa1 = aa[0]
last_aa = aa[-1]
fifth_aa = aa[4]
print("The first amino acid on the chain:", aa1)
print("The last amino acid on the chain: ", last_aa)
print("The 5th amino acid on the chain:  ", fifth_aa)

# Question 2
seq = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
print("TCCGGA" in seq)
print("The restriction site is located between postition", \
      seq.find("TCCGGA") ,"to",(seq.find("TCCGGA") + (len("TCCGGA"))),"of the sequence")