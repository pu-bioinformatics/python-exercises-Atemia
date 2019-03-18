#!/Users/ATEMIA/miniconda3/bin/python

# Question 1
s = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
dna = list(s) # convert the sequence to a list to make it mutable.
complement = {"A":"T", "T":"A", "C":"G", "G":"C" } # create a dictionary to complement.
C = [complement[base] for base in dna]  # complment the sequence
print("The complement sequence is", C)
joined_C = ''.join(C)  # join the sequence
print("The joined sequence is", joined_C)
reverse_complement = joined_C[ : : -1]  # reverse the sequence
print("The revese complement of the sequence is", reverse_complement)
